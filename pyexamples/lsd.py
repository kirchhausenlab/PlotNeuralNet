
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),

    to_Image("image0",s_filer="",n_filer=196,offset="(-5.5,0,0)",height=39.2,depth=39.2,width=2,caption="Raw"),
    to_input('imgs/raw.png', to="(-5.68,-0.58,-1.5)", width=7.82, height=7.82),

    #Encoder

    ############# 1st layer ############
    to_Image("image1",s_filer="",n_filer=196,offset="(-1.6,0,0)",height=39.2,depth=39.2,width=2),

    to_connection("image0", "image1"),

    to_Conv("conv1","","",offset="(-1.1,0,0)",height=39.2,depth=39.2,width=2),

    to_Conv("conv2","","",offset="(-0.6,0,0)",height=39,depth=39,width=2),

    to_Image("image2",s_filer=12,n_filer=192,offset="(-0.1,0,0)",height=38.4,depth=38.4,width=2),

    to_Pool(name="pool_b1",offset="(0,0,0)",to="(image2-east)",width=1,height=19.2,depth=19.2,opacity=0.5),

    ############# 2nd layer ############

    to_Image("image3",s_filer="",n_filer=96,offset="(2.7,0,0)",height=19.2,depth=19.2,width=2),

    to_connection("pool_b1", "image3"),

    to_Conv("conv3","","",offset="(3.2,0,0)",height=19.2,depth=19.2,width=2),

    to_Conv("conv4","","",offset="(3.7,0)",height=19,depth=19,width=2),

    to_Image("image4",s_filer=72,n_filer=92,offset="(4.2,0,0)",height=18.4,depth=18.4,width=2),

    to_Pool(name="pool_b2",offset="(0,0,0)",to="(image4-east)",width=1,height=9.2,depth=9.2,opacity=0.5),

    ############# 3rd layer ############

    to_Image("image5",s_filer="",n_filer=46,offset="(6,0,0)",height=9.2,depth=9.2,width=2),

    to_connection("pool_b2", "image5"),

    to_Conv("conv5","","",offset="(6.5,0,0)",height=9.2,depth=9.2,width=2),

    to_Conv("conv6","","",offset="(7,0,0)",height=9,depth=9,width=2),

    to_Image("image6",s_filer=432,n_filer=42,offset="(7.5,0,0)",height=8.4,depth=8.4,width=2),

    to_Pool(name="pool_b3",offset="(0,0,0)",to="(image6-east)",width=1,height=2.8,depth=2.8,opacity=0.5),


    ############# Bottleneck ############


    to_Image("image7",s_filer="",n_filer=14,offset="(9,0,0)",height=2.8,depth=2.8,width=2),

    to_connection("pool_b3", "image7"),

    to_Conv("conv7","","",offset="(9.5,0,0)",height=2.8,depth=2.8,width=2),

    to_Conv("conv8","","",offset="(10.0,0,0)",height=2.4,depth=2.4,width=2),

    to_Image("image8",s_filer=2592,n_filer=10,offset="(10.5,0,0)",height=2,depth=2,width=2),

    # Encoder

    ############# 1st layer ############

    to_UnPool(name="unpool_b1",offset="(1,0,0)",to="(image8-east)",width=1,height=6.0,depth=6.0,opacity=0.5),

    to_connection("image8", "unpool_b1"),

    to_Image("image9",s_filer="",n_filer=30,offset="(12.1,0,0)",height=6.0,depth=6.0,width=2),

    to_skip( of='image6', to='image9', pos=1.25),

    to_Conv("conv9","","",offset="(12.6,0,0)",height=6.0,depth=6.0,width=2),

    to_Conv("conv10","","",offset="(13.1,0,0)",height=5.6,depth=5.6,width=2),

    to_Image("image10",s_filer=432,n_filer=26,offset="(13.6,0,0)",height=5.2,depth=5.2,width=2),

    ############# 2nd layer ############

    to_UnPool(name="unpool_b2",offset="(1,0,0)",to="(image10-east)",width=1,height=10.4,depth=10.4,opacity=0.5),

    to_connection("image10", "unpool_b2"),

    to_Image("image11",s_filer="",n_filer=52,offset="(15.2,0,0)",height=10.4,depth=10.4,width=2),

    to_skip( of='image4', to='image11', pos=1.25),

    to_Conv("conv11","","",offset="(15.7,0,0)",height=10.4,depth=10.4,width=2),

    to_Conv("conv12","","",offset="(16.2,0,0)",height=10,depth=10,width=2),

    to_Image("image12",s_filer=72,n_filer=48,offset="(16.7,0,0)",height=9.6,depth=9.6,width=2),

    ############# 3rd layer ############

    to_UnPool(name="unpool_b3",offset="(1.4,0,0)",to="(image12-east)",width=1,height=19.2,depth=19.2,opacity=0.5),

    to_connection("image12", "unpool_b3"),

    to_Image("image13",s_filer="",n_filer=96,offset="(18.7,0,0)",height=19.2,depth=19.2,width=2),

    to_skip( of='image2', to='image13', pos=1.25),

    to_Conv("conv13","","",offset="(19.2,0,0)",height=19.2,depth=19.2,width=2),

    to_Conv("conv14","","",offset="(19.7,0,0)",height=18.8,depth=18.8,width=2),

    to_Image("image14",s_filer=12,n_filer=92,offset="(20.2,0,0)",height=18.4,depth=18.4,width=2),

    ############# outputs ############

    to_Conv("conv15","","",offset="(23.5,0,0)",height=18.4,depth=18.4,width=2),

    to_Image("image15",s_filer=3,n_filer="",offset="(24,0,0)",height=18.4,depth=18.4,width=2,caption="LSD[0:3]"),
    to_input('imgs/crops/offsets.png', to="(24,-0.4,-1.05)",width=3.66,height=3.66),
    to_connection("image14", "image15"),

    to_Image("image16",s_filer=3,n_filer="",offset="(26,0,0)",height=18.4,depth=18.4,width=2,caption="LSD[3:6]"),
    to_input('imgs/crops/orthogs.png', to="(26,-0.4,-1.05)",width=3.66,height=3.66),

    to_Image("image17",s_filer=3,n_filer="",offset="(28,0,0)",height=18.4,depth=18.4,width=2,caption="LSD[6:9]"),
    to_input('imgs/crops/diags.png', to="(28,-0.4,-1.05)",width=3.66,height=3.66),

    to_Image("image18",s_filer=1,n_filer="",offset="(30,0,0)",height=18.4,depth=18.4,width=2,caption="LSD[9:10]"),
    to_input('imgs/crops/size.png', to="(30,-0.4,-1.05)",width=3.66,height=3.66),

    to_end()

    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
