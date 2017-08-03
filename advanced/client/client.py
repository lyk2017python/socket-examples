import socket
import os

# Bağlantımızı yönetecek olan socketi 'client' değişkenine attık
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kullanıcıdan bağlanmak istediği ip ve port'u istedik
host = input("Host: ")
port = int(input("Port: "))

# Socket bağlantısını yapmasını istedik.
client.connect((host, port))

while True:
    # 1024 byte'dan fazla olmayacak veri istedik
    gelenMesaj = client.recv(1024)

    print("[CLIENT] Sunucudan gelen mesaj: " + gelenMesaj.decode('utf-8'))

    resminYolu = input("Göndermek istediğiniz resmin yolu: ")
    statinfo = os.stat(resminYolu)
    resminBoyutu = statinfo.st_size

# Socket bağlantısını kapattık.
client.close()