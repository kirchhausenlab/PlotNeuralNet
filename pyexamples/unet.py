
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),

    #Encoder

    ############# 1st layer ############
    to_Image("image1","","",offset="(0,0,0)",height=39.2,depth=39.2,width=2),

    to_Conv("conv1","","",offset="(0.5,0,0)",height=39.2,depth=39.2,width=2),

    to_Conv("conv2","","",offset="(1,0,0)",height=39,depth=39,width=2),

    to_Image("image2","","",offset="(1.5,0,0)",height=38.4,depth=38.4,width=2),

    to_Pool(name="pool_b1",offset="(0,0,0)",to="(image2-east)",width=1,height=19.2,depth=19.2,opacity=0.5),

    ############# 2nd layer ############

    to_Image("image3","","",offset="(3.0,0,0)",height=19.2,depth=19.2,width=2),

    to_connection("pool_b1", "image3"),

    to_Conv("conv3","","",offset="(3.5,0,0)",height=19.2,depth=19.2,width=2),

    to_Conv("conv4","","",offset="(4.0,0)",height=19,depth=19,width=2),

    to_Image("image4","","",offset="(4.5,0,0)",height=18.4,depth=18.4,width=2),

    to_Pool(name="pool_b2",offset="(0,0,0)",to="(image4-east)",width=1,height=9.2,depth=9.2,opacity=0.5),

    ############# 3rd layer ############

    to_Image("image5","","",offset="(6,0,0)",height=9.2,depth=9.2,width=2),

    to_connection("pool_b2", "image5"),

    to_Conv("conv5","","",offset="(6.5,0,0)",height=9.2,depth=9.2,width=2),

    to_Conv("conv6","","",offset="(7,0,0)",height=9,depth=9,width=2),

    to_Image("image6","","",offset="(7.5,0,0)",height=8.4,depth=8.4,width=2),

    to_Pool(name="pool_b3",offset="(0,0,0)",to="(image6-east)",width=1,height=2.8,depth=2.8,opacity=0.5),


    ############# Bottleneck ############


    to_Image("image7","","",offset="(9,0,0)",height=2.8,depth=2.8,width=2),

    to_connection("pool_b3", "image7"),

    to_Conv("conv7","","",offset="(9.5,0,0)",height=2.8,depth=2.8,width=2),

    to_Conv("conv8","","",offset="(10.0,0,0)",height=2.4,depth=2.4,width=2),

    to_Image("image8","","",offset="(10.5,0,0)",height=2,depth=2,width=2),

    # Encoder

    ############# 1st layer ############

    to_UnPool(name="unpool_b1",offset="(1,0,0)",to="(image8-east)",width=1,height=6.0,depth=6.0,opacity=0.5),

    to_connection("image8", "unpool_b1"),

    to_Image("image9","","",offset="(12.1,0,0)",height=6.0,depth=6.0,width=2),

    to_skip( of='image6', to='image9', pos=1.25),

    to_Conv("conv9","","",offset="(12.6,0,0)",height=6.0,depth=6.0,width=2),

    to_Conv("conv10","","",offset="(13.1,0,0)",height=5.6,depth=5.6,width=2),

    to_Image("image10","","",offset="(13.6,0,0)",height=5.2,depth=5.2,width=2),

    ############# 2nd layer ############

    to_UnPool(name="unpool_b2",offset="(1,0,0)",to="(image10-east)",width=1,height=10.4,depth=10.4,opacity=0.5),

    to_connection("image10", "unpool_b2"),

    to_Image("image11","","",offset="(15.2,0,0)",height=10.4,depth=10.4,width=2),

    to_skip( of='image4', to='image11', pos=1.25),

    to_Conv("conv11","","",offset="(15.7,0,0)",height=10.4,depth=10.4,width=2),

    to_Conv("conv12","","",offset="(16.2,0,0)",height=10,depth=10,width=2),

    to_Image("image12","","",offset="(16.7,0,0)",height=9.6,depth=9.6,width=2),

    ############# 3rd layer ############

    to_UnPool(name="unpool_b3",offset="(1.4,0,0)",to="(image12-east)",width=1,height=19.2,depth=19.2,opacity=0.5),

    to_connection("image12", "unpool_b3"),

    to_Image("image13","","",offset="(18.7,0,0)",height=19.2,depth=19.2,width=2),

    to_skip( of='image2', to='image13', pos=1.25),

    to_Conv("conv13","","",offset="(19.2,0,0)",height=19.2,depth=19.2,width=2),

    to_Conv("conv14","","",offset="(19.7,0,0)",height=18.8,depth=18.8,width=2),

    to_Image("image14","","",offset="(20.2,0,0)",height=18.4,depth=18.4,width=2),

    to_end()

    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
