# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


# Dada una ruta run debe separar el del equipo (IP) y la ruta.
def run(smb_path: str) -> tuple:
    host = path = ""
    if smb_path.startswith("//"):
        output = smb_path[2:].split("/", 1)
    else:
        host, path = smb_path.split("/", 1)

    host, path = output
    path = "/" + path

    return host, path


if __name__ == "__main__":
    run("//1.1.1.1/aprende/python")
