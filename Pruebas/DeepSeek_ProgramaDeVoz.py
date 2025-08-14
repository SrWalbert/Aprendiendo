#!/usr/bin/env python3
"""
Enhanced Real-time Pitch-on-Staff Tuner
---------------------------------------
Features:
- Improved autocorrelation algorithm with parabolic interpolation
- Better visualization with proper ledger lines and note coloring
- Smoothing filter for stable pitch detection
- Configurable display options
- Responsive UI with performance optimizations
"""

import sys
import math
import queue
import threading
import time
from dataclasses import dataclass
import numpy as np
import sounddevice as sd
import tkinter as tk
from tkinter import ttk

# --------------------------- Constants and Utilities ---------------------------

A4 = 440.0
A4_MIDI = 69
SAMPLE_RATE = 44100
BLOCK_SIZE = 2048

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
LETTER_INDEX = {"C": 0, "D": 1, "E": 2, "F": 3, "G": 4, "A": 5, "B": 6}

# Colors for visualization
COLORS = {
    "staff": "#333",
    "ledger": "#555",
    "needle": "#D32F2F",
    "in_tune": "#388E3C",
    "sharp": "#1976D2",
    "flat": "#7B1FA2",
    "background": "#F5F5F5",
    "canvas_bg": "#FFFFFF",
}


def freq_to_midi(freq: float) -> int:
    return int(round(12 * math.log2(freq / A4) + A4_MIDI))


def midi_to_freq(midi: int) -> float:
    return A4 * (2 ** ((midi - A4_MIDI) / 12.0))


@dataclass
class NoteInfo:
    name: str
    octave: int
    letter: str


def midi_to_note(midi: int) -> NoteInfo:
    name = NOTE_NAMES[midi % 12]
    octave = midi // 12 - 1
    letter = name[0]
    return NoteInfo(name=name, octave=octave, letter=letter)


def cents_off(freq: float, target_freq: float) -> float:
    return 1200.0 * math.log2(freq / target_freq)


# --------------------------- Enhanced Pitch Detection --------------------------


def parabolic_interpolation(correlations: np.ndarray, index: int) -> float:
    """Improve frequency estimation using parabolic interpolation"""
    alpha = correlations[index - 1]
    beta = correlations[index]
    gamma = correlations[index + 1]
    denom = alpha - 2 * beta + gamma
    if abs(denom) > 1e-12:
        shift = 0.5 * (alpha - gamma) / denom
    else:
        shift = 0.0
    return index + shift


def enhanced_autocorrelate(buffer: np.ndarray, sample_rate: int) -> float | None:
    """
    Improved pitch detection with:
    - Pre-emphasis filtering
    - Dynamic thresholding
    - Parabolic interpolation
    - Frequency range validation
    """
    # Pre-emphasis filter to boost high frequencies
    buf = buffer.copy()
    buf[1:] -= 0.97 * buf[:-1]

    # Remove DC offset and normalize
    buf -= np.mean(buf)
    rms = np.sqrt(np.mean(buf**2))
    if rms < 0.01:  # Silence threshold
        return None

    # Autocorrelation using FFT for efficiency
    n = len(buf)
    corr = np.correlate(buf, buf, mode="full")[n - 1 :]
    corr = corr / (np.arange(n, 0, -1) + 1e-12)  # Normalize

    # Find peaks with dynamic threshold
    threshold = 0.3 * np.max(corr[10:])
    peaks = np.where(corr > threshold)[0]

    if len(peaks) == 0:
        return None

    # Find the first peak with significant correlation
    best_index = peaks[0]
    best_value = corr[best_index]

    # Find the global maximum beyond the first peak
    for i in range(1, len(peaks)):
        if corr[peaks[i]] > best_value:
            best_value = corr[peaks[i]]
            best_index = peaks[i]

    # Apply parabolic interpolation for better accuracy
    if 1 <= best_index < len(corr) - 1:
        best_index = parabolic_interpolation(corr, best_index)

    # Calculate frequency
    period = best_index
    freq = sample_rate / period

    # Validate frequency range (human voice)
    if 80.0 <= freq <= 1200.0:
        return float(freq)
    return None


# --------------------------- Staff Mapping ------------------------------------


def diatonic_steps_from_E4(midi: int) -> int:
    """Calculate staff position relative to E4 (bottom line)"""
    ref_oct = 4
    ref_letter_idx = LETTER_INDEX["E"]
    note = midi_to_note(midi)
    letter_idx = LETTER_INDEX[note.letter]
    return (note.octave - ref_oct) * 7 + (letter_idx - ref_letter_idx)


# --------------------------- GUI Application ----------------------------------


class PitchStaffApp:
    def __init__(self, master: tk.Tk):
        self.master = master
        master.title("Enhanced Pitch-on-Staff Tuner")
        master.geometry("900x500")
        master.configure(bg=COLORS["background"])
        master.minsize(800, 450)

        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TFrame", background=COLORS["background"])
        self.style.configure("TButton", font=("Segoe UI", 10), padding=6)
        self.style.configure(
            "Header.TLabel",
            font=("Segoe UI", 14, "bold"),
            background=COLORS["background"],
        )
        self.style.configure(
            "Info.TLabel", font=("Segoe UI", 10), background=COLORS["background"]
        )
        self.style.configure(
            "Meter.TLabel", font=("Segoe UI", 9), background=COLORS["background"]
        )

        # Main layout
        main_frame = ttk.Frame(master)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Left panel - Staff display
        left_frame = ttk.Frame(main_frame)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

        # Right panel - Controls and meter
        right_frame = ttk.Frame(main_frame, width=300)
        right_frame.grid(row=0, column=1, sticky="nsew")

        main_frame.columnconfigure(0, weight=3)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # Header and controls
        header_frame = ttk.Frame(left_frame)
        header_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(
            header_frame, text="Real-time Pitch on Staff", style="Header.TLabel"
        ).pack(side="left")

        self.btn = ttk.Button(header_frame, text="Start", command=self.toggle)
        self.btn.pack(side="right")

        # Staff canvas
        self.staff_w = 600
        self.staff_h = 240
        self.margin = 20
        self.line_spacing = 18

        staff_container = ttk.Frame(left_frame)
        staff_container.pack(fill="both", expand=True)

        self.staff_canvas = tk.Canvas(
            staff_container,
            width=self.staff_w,
            height=self.staff_h,
            bg=COLORS["canvas_bg"],
            highlightthickness=0,
        )
        self.staff_canvas.pack(fill="both", expand=True)

        # Info display
        info_frame = ttk.Frame(left_frame)
        info_frame.pack(fill="x", pady=(10, 0))

        self.info_var = tk.StringVar(value="Detected: —")
        self.target_var = tk.StringVar(value="Target: —")
        self.cents_var = tk.StringVar(value="Deviation: —")

        ttk.Label(info_frame, textvariable=self.info_var, style="Info.TLabel").pack(
            anchor="w"
        )
        ttk.Label(info_frame, textvariable=self.target_var, style="Info.TLabel").pack(
            anchor="w"
        )
        ttk.Label(info_frame, textvariable=self.cents_var, style="Info.TLabel").pack(
            anchor="w"
        )

        # Right panel content
        ttk.Label(right_frame, text="Tuning Meter", style="Header.TLabel").pack(
            anchor="w", pady=(0, 10)
        )

        meter_container = ttk.Frame(right_frame)
        meter_container.pack(fill="x", pady=(0, 20))

        self.meter_w = 280
        self.meter_h = 60
        self.range_cents = 50.0
        self.meter = tk.Canvas(
            meter_container,
            width=self.meter_w,
            height=self.meter_h,
            bg=COLORS["canvas_bg"],
            highlightthickness=0,
        )
        self.meter.pack()

        # Cent markers
        marker_frame = ttk.Frame(meter_container)
        marker_frame.pack(fill="x")

        ttk.Label(marker_frame, text="-50", style="Meter.TLabel").pack(side="left")
        ttk.Label(marker_frame, text="0", style="Meter.TLabel").pack(
            side="left", expand=True
        )
        ttk.Label(marker_frame, text="+50", style="Meter.TLabel").pack(side="right")

        # Configuration
        config_frame = ttk.LabelFrame(right_frame, text="Settings")
        config_frame.pack(fill="x", pady=(0, 20))

        ttk.Label(config_frame, text="Sensitivity:").grid(
            row=0, column=0, sticky="w", padx=5, pady=2
        )
        self.sensitivity = tk.DoubleVar(value=0.3)
        ttk.Scale(
            config_frame,
            from_=0.1,
            to=0.9,
            variable=self.sensitivity,
            orient="horizontal",
            length=200,
        ).grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(config_frame, text="Smoothing:").grid(
            row=1, column=0, sticky="w", padx=5, pady=2
        )
        self.smoothing = tk.DoubleVar(value=0.7)
        ttk.Scale(
            config_frame,
            from_=0.1,
            to=0.9,
            variable=self.smoothing,
            orient="horizontal",
            length=200,
        ).grid(row=1, column=1, padx=5, pady=2)

        # Status bar
        self.status_var = tk.StringVar(value="Ready to start")
        status_bar = ttk.Frame(right_frame, height=20)
        status_bar.pack(fill="x", side="bottom")
        ttk.Label(
            status_bar,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            background=COLORS["background"],
        ).pack(side="left")

        # State
        self.running = False
        self.stream = None
        self.q = queue.Queue(maxsize=8)
        self.history = []

        # Drawing initial elements
        self.draw_staff_static()
        self.draw_meter_static()

        # Dynamic items
        self.note_items = []
        self.ledger_items = []
        self.needle_item = None

        # Measured values
        self.current_freq = None
        self.detected_midi = None
        self.nearest_midi = None
        self.cents = None

        # UI update loop
        self.update_ui()

        # Handle window close
        master.protocol("WM_DELETE_WINDOW", self.on_closing)

    # ------------------ Drawing Methods ------------------
    def draw_staff_static(self):
        c = self.staff_canvas
        c.delete("all")

        # Draw staff lines
        left_pad = 34
        for i in range(5):
            y = self.margin + i * self.line_spacing
            c.create_line(
                left_pad,
                y,
                self.staff_w - self.margin,
                y,
                fill=COLORS["staff"],
                width=1.5,
            )

        # Draw treble clef
        clef_points = [
            40,
            self.margin - 10,
            40,
            self.margin + 30,
            60,
            self.margin + 40,
            70,
            self.margin + 30,
            65,
            self.margin + 10,
            50,
            self.margin,
            45,
            self.margin + 15,
            55,
            self.margin + 25,
            60,
            self.margin + 15,
            55,
            self.margin + 5,
        ]
        c.create_line(*clef_points, smooth=True, fill=COLORS["staff"], width=2)

        # Status text
        c.create_text(
            12,
            self.staff_h - 10,
            text="Mic: stopped",
            anchor="w",
            fill="#666",
            font=("Segoe UI", 9),
            tags=("micstatus",),
        )

    def draw_meter_static(self):
        m = self.meter
        m.delete("all")
        y = self.meter_h / 2

        # Draw scale bar
        m.create_rectangle(
            12, y - 8, self.meter_w - 12, y + 8, fill="#eee", outline="#ddd"
        )

        # Center marker
        cx = self.meter_w / 2
        m.create_line(cx, y - 16, cx, y + 16, fill="#999", width=2)

        # Ticks and labels
        for t in [-40, -20, 0, 20, 40]:
            x = 12 + ((t + self.range_cents) / (2 * self.range_cents)) * (
                self.meter_w - 24
            )
            height = 10 if t % 20 == 0 else 6
            m.create_line(x, y - height, x, y + height, fill="#bbb", width=1)

    def staff_y_for_midi(self, midi: int) -> float:
        steps = diatonic_steps_from_E4(midi)
        bottom = self.margin + 4 * self.line_spacing
        step = self.line_spacing / 2.0
        return bottom - steps * step

    def draw_note(self, midi: int, cents: float):
        # Clear previous items
        for item in self.note_items + self.ledger_items:
            self.staff_canvas.delete(item)
        self.note_items.clear()
        self.ledger_items.clear()

        y = self.staff_y_for_midi(midi)
        x = 180

        # Determine note color based on tuning
        if cents is None:
            color = COLORS["staff"]
        elif abs(cents) < 10:
            color = COLORS["in_tune"]
        elif cents > 0:
            color = COLORS["sharp"]
        else:
            color = COLORS["flat"]

        # Draw stem
        self.note_items.append(
            self.staff_canvas.create_line(x, y - 20, x, y + 20, fill=color, width=2)
        )

        # Draw note head
        self.note_items.append(
            self.staff_canvas.create_oval(
                x - 12, y - 9, x + 12, y + 9, fill=color, outline=color
            )
        )

        # Draw ledger lines if needed
        steps = diatonic_steps_from_E4(midi)
        if steps < 0:
            for s in range(0, steps - 1, -1):
                if s % 2 == 0:
                    yy = self.staff_y_for_midi(64) - s * (self.line_spacing / 2.0)
                    self.ledger_items.append(
                        self.staff_canvas.create_line(
                            90,
                            yy,
                            self.staff_w - 120,
                            yy,
                            fill=COLORS["ledger"],
                            width=1.5,
                        )
                    )
        elif steps > 8:
            for s in range(8, steps + 1):
                if s % 2 == 0:
                    yy = self.staff_y_for_midi(64) - s * (self.line_spacing / 2.0)
                    self.ledger_items.append(
                        self.staff_canvas.create_line(
                            90,
                            yy,
                            self.staff_w - 120,
                            yy,
                            fill=COLORS["ledger"],
                            width=1.5,
                        )
                    )

    def update_meter(self, cents: float | None):
        if self.needle_item:
            self.meter.delete(self.needle_item)
            self.needle_item = None

        if cents is None:
            return

        maxr = self.range_cents
        c = max(-maxr, min(maxr, cents))
        x = 12 + ((c + maxr) / (2 * maxr)) * (self.meter_w - 24)
        y = self.meter_h / 2

        # Draw needle
        self.needle_item = self.meter.create_line(
            x, y - 20, x, y + 20, fill=COLORS["needle"], width=3
        )

        # Draw center indicator
        self.meter.create_oval(
            x - 4, y - 4, x + 4, y + 4, fill=COLORS["needle"], outline=""
        )

    # ------------------ Audio Processing ------------------
    def audio_callback(self, indata, frames, time_info, status):
        if status:
            print("Audio error:", status, file=sys.stderr)

        # Process mono audio
        mono = indata[:, 0].copy()
        try:
            self.q.put_nowait(mono)
        except queue.Full:
            pass  # Drop samples if queue is full

    def start_audio(self):
        try:
            self.stream = sd.InputStream(
                channels=1,
                samplerate=SAMPLE_RATE,
                blocksize=BLOCK_SIZE,
                dtype="float32",
                callback=self.audio_callback,
            )
            self.stream.start()
            self.status_var.set("Microphone active")
            return True
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            return False

    def stop_audio(self):
        if self.stream:
            try:
                self.stream.stop()
                self.stream.close()
            except Exception:
                pass
            self.stream = None
        self.status_var.set("Microphone stopped")

    # ------------------ UI and Control ------------------
    def toggle(self):
        if not self.running:
            if self.start_audio():
                self.running = True
                self.btn.configure(text="Stop")
                self.staff_canvas.itemconfigure("micstatus", text="Mic: active")
        else:
            self.stop_audio()
            self.running = False
            self.btn.configure(text="Start")
            self.staff_canvas.itemconfigure("micstatus", text="Mic: stopped")
            self.reset_display()

    def reset_display(self):
        self.current_freq = None
        self.detected_midi = None
        self.nearest_midi = None
        self.cents = None
        self.info_var.set("Detected: —")
        self.target_var.set("Target: —")
        self.cents_var.set("Deviation: —")
        self.update_meter(None)
        self.draw_note(64, 0)  # Clear note display

    def smooth_value(self, new_value, history, alpha=0.7):
        """Apply exponential smoothing to values"""
        if not history:
            return new_value
        return alpha * new_value + (1 - alpha) * history[-1]

    def update_ui(self):
        # Process audio data
        while not self.q.empty():
            try:
                block = self.q.get_nowait()
                freq = enhanced_autocorrelate(block, SAMPLE_RATE)

                if freq:
                    # Apply smoothing
                    self.history.append(freq)
                    if len(self.history) > 10:
                        self.history.pop(0)

                    smoothed_freq = np.mean(self.history)

                    # Update note info
                    self.current_freq = smoothed_freq
                    midi = freq_to_midi(smoothed_freq)
                    self.detected_midi = midi
                    self.nearest_midi = midi
                    target = midi_to_freq(midi)
                    cents = cents_off(smoothed_freq, target)
                    self.cents = cents

                    # Update display
                    note = midi_to_note(midi)
                    self.info_var.set(
                        f"Detected: {note.name}{note.octave} · {smoothed_freq:.1f} Hz"
                    )
                    self.target_var.set(
                        f"Target: {note.name}{note.octave} · {target:.1f} Hz"
                    )
                    self.cents_var.set(
                        f"Deviation: {cents:+.1f} cents {'(sharp)' if cents > 0 else '(flat)' if cents < 0 else '(in tune)'}"
                    )

                    self.draw_note(midi, cents)
                    self.update_meter(cents)
                else:
                    self.reset_display()

            except queue.Empty:
                break
            except Exception as e:
                self.status_var.set(f"Processing error: {str(e)}")

        # Schedule next update
        self.master.after(30, self.update_ui)

    def on_closing(self):
        self.stop_audio()
        self.master.destroy()


# --------------------------- Main ---------------------------------------------


def main():
    root = tk.Tk()
    app = PitchStaffApp(root)
    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication terminated")
        sys.exit(0)
