import download_request

ls = """dace9a6b-8e6c-4189-830c-61aa672258a1
407cc207-fafc-4884-981f-c14ae5b53196
3f4f23e9-c77f-4675-8b7c-371e773170a8
efedc116-3ba9-4012-9614-83ec2c7448bd
543554fa-5467-4ea0-982d-83edf9be6a9d
4d9377c6-0fcc-43c5-8f73-b27fddbeb0bc
0153bff4-3dad-443e-9ba1-3e315f1f6a03
5a15feec-d158-45bb-beaf-ffb1bce50cea
5ccf840a-7e2b-4517-9c15-da0f543e4ac6
d96ee2e9-5af8-4b19-ae81-1378175d2e35
6f42332c-f29e-4917-afad-974882045c2e
c01e6267-7b2a-4864-a57c-ecda9fba1b9b
1b356c50-8ef3-48d9-983c-4a4f9fd91528
01ebdc4f-db7a-4119-9335-284282176732
1cb4a101-c894-48ee-97a7-8cd49bbfbc99"""

l = ls.split("\n")
att = ["Tag"]
for i in l:
    att = download_request.get_attribute(table="BURN_Master_ImgCollections",guid=i,attr=att)
    print(att)