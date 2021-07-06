import paramiko
import os


# host = "s-9f90ccda8d9d4fb28.server.transfer.us-west-2.amazonaws.com"
# port = 22
# transport = paramiko.Transport((host, port))
# username = "canvas_user"
# mykey = paramiko.RSAKey.from_private_key_file("C:\\Users\\monis\\Downloads\\sFTP_Credentials\\sFTP_Credentials\\new_pem_file.pem", password="CWW2021")
# print("Connecting...")
# transport.connect(username = username, pkey = mykey)
# sftp = paramiko.SFTPClient.from_transport(transport)
# print("Connected.")
# print(sftp.listdir())
# print(sftp.getcwd())
# print(sftp.getcwd())
# sftp.put("C:\\Users\\monis\\Downloads\\sFTP_Credentials\\sFTP_Credentials\\TT.xlsx","/impressions_costs/TT.xlsx")
# sftp.close()
# transport.close()
# print("Closed connection.")


def sftp_uploader(hostname, port, username, pkey_path, passphrase, sftp_directory, local_directory):
    import paramiko
    import os
    transport = paramiko.Transport((hostname, port))
    mykey = paramiko.RSAKey.from_private_key_file(pkey_path, password=passphrase)
    print("Connecting to SFTP server...")
    transport.connect(username=username, pkey=mykey)
    sftp = paramiko.SFTPClient.from_transport(transport)
    print("Connected to SFTP server.")
    print(sftp.listdir())
    file_name = os.path.basename(local_directory)
    sftp_directory=sftp_directory+"/"+file_name
    sftp.put(local_directory, sftp_directory)
    sftp.close()
    transport.close()
    print("Closed connection.")
    return f"Files are uploaded successfully to the directory {sftp_directory}"



# sftp_uploader("s-9f90ccda8d9d4fb28.server.transfer.us-west-2.amazonaws.com",22,"canvas_user","C:\\Users\\monis\\Downloads\\sFTP_Credentials\\sFTP_Credentials\\new_pem_file.pem","CWW2021","/impressions_costs","C:\\Users\\monis\\Downloads\\sFTP_Credentials\\sFTP_Credentials\\TT.xlsx")
