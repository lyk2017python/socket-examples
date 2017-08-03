import socket

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

    # İstemci'nin göndermek istediği mesajı soralım.
    mesaj = input("Gidecek Mesaj: ")

    # Bu mesajı encode edip sunucuya gönderelim.
    client.send(mesaj.encode('utf-8'))

    if mesaj == "exit":
        break

# Socket bağlantısını kapattık.
client.close()