computers = {
    "pc1": {
        "os": "Windows 10",
        "processor": "ADM Phenom II",
        "ram": "8 GB",
        "motherboard": "MSI87343",
        "hdd": "1Tb",
    },
    "pc2": {
        "os": "Windows 10",
        "processor": "ADM Phenom I",
        "ram": "4 Gb",
        "motherboard": "MSI845656",
        "hdd": "512Gb"
    },
    "pc3": {
        "os": "Windows 7",
        "processor": "ADM Phenom II",
        "ram": "4 Gb",
        "motherboard": "Asus-4565",
        "hdd": "1Tb",
    },
}

device = input("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")

print(computers[device][parameter])
