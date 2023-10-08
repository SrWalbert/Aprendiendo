from textblob import TextBlob


# Pendiente a optimizar
class SentimentAnalyzer:
    def analyze_sentiment(self, text: str) -> str:
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        return self.map_polarity_to_emotion(polarity)

    def map_polarity_to_emotion(self, polarity: float) -> str:
        if -1 <= polarity <= -0.5:
            return "Negativo"
        elif -0.5 < polarity < -0.1:
            return "Algo negativo"
        elif -0.1 <= polarity < 0.1:
            return "Neutral"
        elif 0.1 <= polarity <= 0.5:
            return "Algo positivo"
        else:
            return "Positivo"


class ConsoleUI:
    def run(self):
        analyzer = SentimentAnalyzer()
        while True:
            text_to_analyze = input("Ingresa tu texto: ")
            if text_to_analyze.lower() == "salir":
                break
            result = analyzer.analyze_sentiment(text_to_analyze)
            print(result)


if __name__ == "__main__":
    app = ConsoleUI()
    app.run()
