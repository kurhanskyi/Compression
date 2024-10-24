import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from compressors.rle_compressor import RLECompressor
from utils.file_handler import FileHandler
from utils.checksum import calculate_checksum

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Особисто я зробив ліміт 16 МБ

compressor = RLECompressor()
file_handler = FileHandler()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='Немає частини файлу')

        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='Не вибраний файл')

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            original_data = file_handler.read_file(file_path)
            original_size = len(original_data)
            original_checksum = calculate_checksum()

            compressed_data = compressor.compress(original_data)
            compressed_size = len(compressed_data)
            compressed_checksum = calculate_checksum()

            compression_ratio = compressor.get_compression_ratio(original_size, compressed_size)

            compressed_filename = f"compressed_{filename}"
            compressed_path = os.path.join(app.config['UPLOAD_FOLDER'], compressed_filename)
            file_handler.write_file(compressed_path, compressed_data)

            return render_template('result.html',
                                   original_filename=filename,
                                   compressed_filename=compressed_filename,
                                   original_size=original_size,
                                   compressed_size=compressed_size,
                                   compression_ratio=compression_ratio,
                                   original_checksum=original_checksum,
                                   compressed_checksum=compressed_checksum)

    return render_template('index.html')


@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True, port=1111)
    calculate_checksum()