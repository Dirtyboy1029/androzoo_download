# androzoo_download
download apk file from androzoo according to year and benign/malware
Step1:
if get malware:
## malware  10<=vt_scan<80
    python get_sha256_csv.py 2020 --vt_detection 10 --upper 80 
elif get benign
## benign :vt_scan==0
    python get_sha256_csv.py 2020 --vt_detection 0
    
Step2:
## from csv get sha256.txt
   python select_sample.py


Step3:
##download apk
   python androzoo_download.py
