import subprocess
import base64

def main():
    result = ""

    hostname = subprocess.Popen(args="hostname", stdin = subprocess.PIPE, stdout= subprocess.PIPE, stderr = subprocess.PIPE, shell = True).stdout.read().decode()
    result += "Hostname :\n" + hostname + "\n"

    user = subprocess.Popen(args="net user", stdin = subprocess.PIPE, stdout= subprocess.PIPE, stderr = subprocess.PIPE, shell = True).stdout.read().decode()
    result += "User :\n" + user + "\n"

    privillage = subprocess.Popen(args="whoami /priv", stdin = subprocess.PIPE, stdout= subprocess.PIPE, stderr = subprocess.PIPE, shell = True).stdout.read().decode()
    result += "Privillage :\n" + privillage + "\n"

    print(result)

    text = result.encode("ascii")
    byte = base64.b64encode(text)

    message = byte.decode("ascii")
    print(f"Encode result : {message}")

if __name__ == "__main__":
    main()