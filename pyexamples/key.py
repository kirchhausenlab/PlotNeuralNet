
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),

    to_Image("image0","","",height=10,depth=10,width=1.5,caption="Image"),

    to_Conv("conv","","",offset="(2.0,0,0)",height=10,depth=10,width=1.5,caption="Conv"),

    to_Pool(name="pool",offset="(1.7,0,0)",to="(conv-east)",height=10,depth=10,width=1.5,caption="Down"),

    to_UnPool(name="unpool",offset="(1.7,0,0)",to="(pool-east)",height=10,depth=10,width=1.5,caption="Up"),

    to_Image("image1","","",offset="(7.3,0,0)",height=10,depth=10,width=1.5,fopacity=0.0,bopacity=0.0),
    to_Image("image2","","",offset="(8.55,0,0)",height=10,depth=10,width=1.5,fopacity=0.0,bopacity=0.0,caption="Input"),
    to_Image("image3","","",offset="(9.3,0,0)",height=10,depth=10,width=1.5,fopacity=0.0,bopacity=0.0),
    to_Image("image4","","",offset="(9.8,0,0)",height=10,depth=10,width=1.5,fopacity=0.0,bopacity=0.0),
    to_Image("image5","","",offset="(11.1,0,0)",height=10,depth=10,width=1.5,fopacity=0.0,bopacity=0.0,caption="Skip"),
    to_Image("image6","","",offset="(11.8,0,0)",height=10,depth=10,width=1.5,fopacity=0.0,bopacity=0.0),

    to_connection("image1", "image3"),
    to_skip_key("image4", "image6"),

    to_end()

    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
