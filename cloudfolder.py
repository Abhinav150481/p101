import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token 

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token) 

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)        

def main():
        access_token ='sl.BJAHlBQWFNN3Cw7h2oDNIHbK6GO1hXZGW95LTJk_s2jo4obsI_6YK5H6oPEwDroy7B71RnttmpFXD1Lva5ECqb1kjikwJ_USj7p8PoDmK3nRVGVC8sGln8fRk9L3hv8xA3eeV0I'
        transferData = TransferData(access_token)
        
        file_from = input("enter the file path ot transfer :- ")
        file_to = input("enter to full path to upload to dropbox")

        transferData.upload_file(file_from,file_to)
        print("file has been moved")
        
main()



