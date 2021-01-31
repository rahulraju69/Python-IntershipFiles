import speedtest
st=speedtest.Speedtest()

print("Download speed:",st.download())
print("Upload speed:",st.upload())
