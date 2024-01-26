fn cifrado_cesar(texto: &str, desplazamiento: i32) -> String {
    texto.chars().map(|c| {
            if c.is_alphabetic() {
                let inicio = if c.is_uppercase() { 'A' } else { 'a' } as i32;
                // Convertir el caracter a un número (0-25), aplicar desplazamiento y volver a convertir a caracter
                let mut desplazado = (c as i32 - inicio + desplazamiento) % 26;
                if desplazado < 0 {
                    desplazado += 26;
                }
                (inicio + desplazado) as u8 as char
            } else {
                // Si no es una letra, dejar el caracter como está
                c
            }
        }
    ).collect()
}

fn main() {
    let texto = "Hola Mundo";
    let desplazamiento = 3; // Puede ser cualquier número
    let texto_cifrado = cifrado_cesar(texto, desplazamiento);
    println!("Texto cifrado: {}", texto_cifrado);
}
