import hashlib
import os
import pathlib
import struct
import sys
import datetime
import struct

def mse_ksa():
    key = [
        0x1E, 0x87, 0x78, 0x1B, 0x8D, 0xBA, 0xA8, 0x44, 0xCE, 0x69,
        0x70, 0x2C, 0x0C, 0x78, 0xB7, 0x86, 0xA3, 0xF6, 0x23, 0xB7,
        0x38, 0xF5, 0xED, 0xF9, 0xAF, 0x83, 0x53, 0x0F, 0xB3, 0xFC,
        0x54, 0xFA, 0xA2, 0x1E, 0xB9, 0xCF, 0x13, 0x31, 0xFD, 0x0F,
        0x0D, 0xA9, 0x54, 0xF6, 0x87, 0xCB, 0x9E, 0x18, 0x27, 0x96,
        0x97, 0x90, 0x0E, 0x53, 0xFB, 0x31, 0x7C, 0x9C, 0xBC, 0xE4,
        0x8E, 0x23, 0xD0, 0x53, 0x71, 0xEC, 0xC1, 0x59, 0x51, 0xB8,
        0xF3, 0x64, 0x9D, 0x7C, 0xA3, 0x3E, 0xD6, 0x8D, 0xC9, 0x04,
        0x7E, 0x82, 0xC9, 0xBA, 0xAD, 0x97, 0x99, 0xD0, 0xD4, 0x58,
        0xCB, 0x84, 0x7C, 0xA9, 0xFF, 0xBE, 0x3C, 0x8A, 0x77, 0x52,
        0x33, 0x55, 0x7D, 0xDE, 0x13, 0xA8, 0xB1, 0x40, 0x87, 0xCC,
        0x1B, 0xC8, 0xF1, 0x0F, 0x6E, 0xCD, 0xD0, 0x83, 0xA9, 0x59,
        0xCF, 0xF8, 0x4A, 0x9D, 0x1D, 0x50, 0x75, 0x5E, 0x3E, 0x19,
        0x18, 0x18, 0xAF, 0x23, 0xE2, 0x29, 0x35, 0x58, 0x76, 0x6D,
        0x2C, 0x07, 0xE2, 0x57, 0x12, 0xB2, 0xCA, 0x0B, 0x53, 0x5E,
        0xD8, 0xF6, 0xC5, 0x6C, 0xE7, 0x3D, 0x24, 0xBD, 0xD0, 0x29,
        0x17, 0x71, 0x86, 0x1A, 0x54, 0xB4, 0xC2, 0x85, 0xA9, 0xA3,
        0xDB, 0x7A, 0xCA, 0x6D, 0x22, 0x4A, 0xEA, 0xCD, 0x62, 0x1D,
        0xB9, 0xF2, 0xA2, 0x2E, 0xD1, 0xE9, 0xE1, 0x1D, 0x75, 0xBE,
        0xD7, 0xDC, 0x0E, 0xCB, 0x0A, 0x8E, 0x68, 0xA2, 0xFF, 0x12,
        0x63, 0x40, 0x8D, 0xC8, 0x08, 0xDF, 0xFD, 0x16, 0x4B, 0x11,
        0x67, 0x74, 0xCD, 0x0B, 0x9B, 0x8D, 0x05, 0x41, 0x1E, 0xD6,
        0x26, 0x2E, 0x42, 0x9B, 0xA4, 0x95, 0x67, 0x6B, 0x83, 0x98,
        0xDB, 0x2F, 0x35, 0xD3, 0xC1, 0xB9, 0xCE, 0xD5, 0x26, 0x36,
        0xF2, 0x76, 0x5E, 0x1A, 0x95, 0xCB, 0x7C, 0xA4, 0xC3, 0xDD,
        0xAB, 0xDD, 0xBF, 0xF3, 0x82, 0x53
    ]
    sbox = list(range(256))
    j = 0
    for i in range(256):
        j = (j + sbox[i] + key[i]) % 256
        tmp = sbox[i]
        sbox[i] = sbox[j]
        sbox[j] = tmp
    return sbox

def rc4(data):
    sbox = mse_ksa()
    out = bytearray(len(data))
    i = 0
    j = 0
    for k in range(len(data)):
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        tmp = sbox[i]
        sbox[i] = sbox[j]
        sbox[j] = tmp
        val = sbox[(sbox[i] + sbox[j]) % 256]
        out[k] = val ^ data[k]

    return out

def create_entries(hashed_file):
    with open('./metadata-template', 'rb') as f:
        new_hash = pathlib.Path(hashed_file).name
        new_detection = "Trojan:Win64/Generic.D!sC0rD.N!tR0"
        new_date = datetime.datetime.now()
        new_path_str = r"\\?\C:\Users\adminganteng\Downloads\DiscordNitroCodeGenerator.py"

        header = rc4(f.read(0x3c))
        data1_len, data2_len = struct.unpack_from('<II', header, 0x28)

        data1 = rc4(f.read(data1_len))
        expected_date = new_date + datetime.timedelta(hours=7)
        filetime = (int(expected_date.timestamp() * 1000000) + 11644473600000000) * 10
        struct.pack_into('<Q', data1, 0x20, filetime)

        data1[0x34:] = new_detection.encode('utf8')

        data2 = rc4(f.read(data2_len))

        o = 8
        data = data2[o:]
        pos = data.find(b'\x00\x00\x00') + 1
        data = bytearray(new_path_str.encode('utf-16le')) + data[pos:]
        pos = data.find(b'\x00\x00\x00') + 1

        pos += 4  # skip number of entries field
        type_len = data[pos:].find(b'\x00')
        pos += type_len + 1
        pos += (4 - pos) % 4  # skip padding bytes
        pos += 4  # skip additional metadata
        data[pos:pos + 20] = bytes.fromhex(new_hash.lower())
        data2 = data2[:o] + data

        filename = f'{{{os.urandom(4).hex().upper()}-0000-0000-{os.urandom(2).hex().upper()}-{os.urandom(6).hex().upper()}}}'
        pathlib.Path(f'./ProgramData/Microsoft/Windows Defender/Quarantine/Entries/').mkdir(parents=True, exist_ok=True)
        with open(f'./ProgramData/Microsoft/Windows Defender/Quarantine/Entries/{filename}', 'wb') as f2:
            struct.pack_into('<II', header, 0x28, len(data1), len(data2))
            f2.write(rc4(header))
            f2.write(rc4(data1))
            f2.write(rc4(data2))
            f2.write(f.read())
        print(f'Entries: {filename}')
    return './ProgramData/Microsoft/Windows Defender/Quarantine/Entries/{}'.format(filename)

def create_encrypted_malware(file):
    with open(file, 'rb') as f:
        file_data = f.read()

    old_len = len(file_data)
    file_data = b"\x03\x00\x00\x00\x02\x00\x00\x00\xa4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x04\x80\x14\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00L\x00\x00\x00\x01\x05\x00\x00\x00\x00\x00\x05\x15\x00\x00\x00$Y_\xf6\x94Y\xff\xfa;\x8e\x97{\xe9\x03\x00\x00\x01\x05\x00\x00\x00\x00\x00\x05\x15\x00\x00\x00$Y_\xf6\x94Y\xff\xfa;\x8e\x97{\xe9\x03\x00\x00\x02\x00X\x00\x03\x00\x00\x00\x00\x00\x14\x00\xff\x01\x1f\x00\x01\x01\x00\x00\x00\x00\x00\x05\x12\x00\x00\x00\x00\x00\x18\x00\xff\x01\x1f\x00\x01\x02\x00\x00\x00\x00\x00\x05 \x00\x00\x00 \x02\x00\x00\x00\x00$\x00\xff\x01\x1f\x00\x01\x05\x00\x00\x00\x00\x00\x05\x15\x00\x00\x00$Y_\xf6\x94Y\xff\xfa;\x8e\x97{\xe9\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" + file_data
    ba = bytearray(file_data)
    sd_len = struct.unpack_from('<I', file_data, 0x8)[0]
    struct.pack_into('<Q', ba, sd_len + 0x1C, old_len)
    encrypted_data = rc4(ba)

    output_filename = hashlib.sha1(file_data).hexdigest().upper()
    pathlib.Path(f'./ProgramData/Microsoft/Windows Defender/Quarantine/ResourceData/{output_filename[:2]}').mkdir(parents=True, exist_ok=True)
    with open(f'./ProgramData/Microsoft/Windows Defender/Quarantine/ResourceData/{output_filename[:2]}/{output_filename}', 'wb') as f:
        f.write(encrypted_data)
    print(f'Encrypted: {output_filename}')
    return './ProgramData/Microsoft/Windows Defender/Quarantine/ResourceData/{}/{}'.format(output_filename[:2], output_filename)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 encrypt.py <file>")
        sys.exit(1)

    if len(sys.argv) > 2:
        for i in range(1, len(sys.argv)-1):
            hashed_file = create_encrypted_malware(sys.argv[i])
            create_entries(hashed_file)
    else:
        hashed_file = create_encrypted_malware(sys.argv[1])
        create_entries(hashed_file)
