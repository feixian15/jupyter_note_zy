def stage(in_channel, out_channel):  
        return nn.Sequential(
            nn.Conv2d(in_channels=in_channel, out_channels=out_channel, kernel_size=3, stride=1,padding=1),
            nn.BatchNorm2d(out_channel),
            nn.ReLU(),
            nn.Conv2d(in_channels=out_channel, out_channels=out_channel, kernel_size=3, stride=1,padding=1),
            nn.BatchNorm2d(out_channel),
            nn.ReLU()
        ) 
def upsample(in_channel, out_channel):
    return nn.ConvTranspose2d(in_channel,out_channel,2,2)

class Unet(nn.Module):
    def __init__(self, channels, classes):
        super(Unet,self).__init__()
        self.conv1 = stage(3, 32)
        self.conv2 = stage(32, 64)
        self.conv3 = stage(64, 128)
        self.conv4 = stage(128, 256)
        self.conv5 = stage(256, 512)
        
        self.upsample54 = upsample(512,256)
        self.upsample43 = upsample(256,128)
        self.upsample32 = upsample(128,64)
        self.upsample21 = upsample(64,32)
        
        self.conv4_m = stage(512, 256)
        self.conv3_m = stage(256, 128)
        self.conv2_m = stage(128, 64)
        self.conv1_m = stage(64, 32)
        
        self.final = nn.Sequential(
            nn.Conv2d(32,classes,1,1),
            nn.Softmax2d()
        )
        
        self.maxpool = nn.MaxPool2d(2,2)
    
    def forward(self, x):
        conv1 = self.conv1(x)
        conv2 = self.conv2(self.maxpool(conv1))
        conv3 = self.conv3(self.maxpool(conv2))
        conv4 = self.conv4(self.maxpool(conv3))
        conv5 = self.conv5(self.maxpool(conv4))
        
        conv4_m = self.conv4_m(torch.cat((conv4,self.upsample54(conv5)),1))
        conv3_m = self.conv3_m(torch.cat((conv3,self.upsample43(conv4_m)),1))
        conv2_m = self.conv2_m(torch.cat((conv2,self.upsample32(conv3_m)),1))
        conv1_m = self.conv1_m(torch.cat((conv1,self.upsample21(conv2_m)),1))
        
        return self.final(conv1_m)