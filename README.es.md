<div align="center">
   <img src="src/img/icon.png" alt="CS2 NoFlash" width="200" height="200">
   <h1>🌟 CS2 NoFlash 🌟</h1>
   <p>Tu herramienta definitiva anti-flash para Counter-Strike 2</p>
   <a href="#características"><strong>Características</strong></a> •
   <a href="#instalación"><strong>Instalación</strong></a> •
   <a href="#uso"><strong>Uso</strong></a> •
   <a href="#personalización"><strong>Personalización</strong></a> •
   <a href="#solución-de-problemas"><strong>Solución de problemas</strong></a> •
   <a href="#contribuir"><strong>Contribuir</strong></a>
   <br><br>
   <p><strong>🌍 Traducciones:</strong></p>
   <a href="README.ru.md"><img src="https://img.shields.io/badge/lang-Russian-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.fr.md"><img src="https://img.shields.io/badge/lang-French-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.es.md"><img src="https://img.shields.io/badge/lang-Spanish-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.uk-UA.md"><img src="https://img.shields.io/badge/lang-Ukrainian-purple?style=for-the-badge&logo=googletranslate"></a>
   <a href="README.pl.md"><img src="https://img.shields.io/badge/lang-Polish-purple?style=for-the-badge&logo=googletranslate"></a>
</div>

---

# Resumen
CS2 NoFlash es una herramienta automatizada diseñada para Counter-Strike 2 que evita que el jugador sea completamente cegado al ajustar automáticamente los valores alfa de las granadas flash en el juego.

## Características
- **Protección Anti-Flash:** Ajusta automáticamente el valor alfa de la granada flash a 0, evitando que el jugador sea completamente cegado.
- **Adjunto al Proceso:** Se adjunta al proceso cs2.exe y lee los valores de memoria para aplicar cambios en tiempo real.
- **Comprobador de Actualizaciones:** Verifica automáticamente la última versión y notifica al usuario si hay una actualización disponible.
- **Registro de Errores:** Registra errores y eventos importantes en un archivo de registro para fines de depuración.

## Instalación
1. **Clonar el Repositorio:**
   
bash
   git clone https://github.com/Jesewe/cs2-noflash.git
   cd cs2-noflash


2. **Instalar Dependencias:**
   
bash
   pip install -r requirements.txt


3. **Ejecutar el Script:**
   
bash
   python main.py


## Uso
1. Asegúrate de que Counter-Strike 2 esté en ejecución.
2. Ejecuta el script utilizando el comando anterior.
3. El script verificará automáticamente las actualizaciones y obtendrá los offsets necesarios de las fuentes proporcionadas.
4. La protección NoFlash comenzará automáticamente, reduciendo el efecto de la granada flash al mínimo.

## Personalización
- **Directorio de Registro:** Los archivos de registro se guardan en el directorio %LOCALAPPDATA%\Requests\ItsJesewe\crashes de forma predeterminada. Puedes cambiar esto modificando la variable LOG_DIRECTORY en el script.

## Solución de problemas
- **Error al Obtener Offsets:** Asegúrate de tener una conexión a internet activa y que las URL de origen sean accesibles.
- **No se Pudo Abrir cs2.exe:** Asegúrate de que el juego esté en ejecución y de tener los permisos necesarios.
- **Errores Inesperados:** Consulta el archivo de registro ubicado en el directorio de registro para más detalles.

## Contribuir
¡Las contribuciones son bienvenidas! Por favor, abre un problema o envía un pull request en el [repositorio de GitHub](https://github.com/Jesewe/cs2-noflash).

## Descargo de responsabilidad
Este script es solo para fines educativos. El uso de trampas o hacks en juegos en línea va en contra de los términos de servicio de la mayoría de los juegos y puede resultar en prohibiciones u otras sanciones. Usa este script bajo tu propio riesgo.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.