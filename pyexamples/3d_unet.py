import sys
from pycore import tikzeng
from pycore import blocks

ADD_INPUT_OUTPUT = True
ADD_DIMENSIONS = False
ADD_CAPTIONS = False

arch = [
    tikzeng.to_head('..'),
    tikzeng.to_cor(),
    tikzeng.to_begin(),
]

if ADD_INPUT_OUTPUT:
    arch.extend(
        [
            # put many images to represent 3d
            *[tikzeng.to_input(
                'imgs/raw_input.png',
                to=f"({-6.0 + 0.1*i},-0.58,-1.5)",
                width=7.8,
                height=7.8) for i in range(7)
              ],
            tikzeng.to_Image(
                "image0",
                s_filer="204\\^{}3" if ADD_DIMENSIONS else "",
                n_filer=1 if ADD_DIMENSIONS else "",
                offset="(-5.5,0,0)",
                height=39.2,
                depth=39.2,
                width=4,
                caption="Raw" if ADD_CAPTIONS else ""),
        ]
    )

# Encoder

############# 1st layer ############
# tikzeng.to_Image(
# "image1",
# s_filer="",
# n_filer=32,
# offset="(-1.6,0,0)",
# height=39.2,
# depth=39.2,
# width=2),

# tikzeng.to_connection("image0", "image1"),

arch.extend(
    [
        tikzeng.to_Conv(
            "conv1",
            "",
            n_filer=32 if ADD_DIMENSIONS else "",
            offset="(-1.1,0,0)",
            height=39.2,
            depth=39.2,
            width=2),

        tikzeng.to_Conv(
            "conv2",
            "",
            # n_filer=32,
            "",
            offset="(-0.6,0,0)",
            height=39,
            depth=39,
            width=2),

        tikzeng.to_Image(
            "image2",
            s_filer="200\\^{}3" if ADD_DIMENSIONS else "",
            n_filer="",
            offset="(-0.1,0,0)",
            height=38.4,
            depth=38.4,
            width=2),

        # tikzeng.to_connection("image0", "image2"),

        tikzeng.to_Pool(
            name="pool_b1",
            s_filer="100\\^{}3" if ADD_DIMENSIONS else "",
            offset="(0,0,0)",
            to="(image2-east)",
            width=2,
            height=19.2,
            depth=19.2,
            opacity=0.5),

        ############# 2nd layer ############

        # tikzeng.to_Image(
        # "image3",
        # s_filer="",
        # n_filer=64,
        # offset="(2.7,0,0)",
        # height=19.2,
        # depth=19.2,
        # width=2),

        # tikzeng.to_connection("pool_b1", "image3"),

        tikzeng.to_Conv(
            "conv3",
            n_filer=64 if ADD_DIMENSIONS else "",
            s_filer="",
            offset="(3.2,0,0)",
            height=19.2,
            depth=19.2,
            width=2),

        tikzeng.to_connection("pool_b1", "conv3"),

        tikzeng.to_Conv(
            "conv4",
            # n_filer=64,
            n_filer="",
            s_filer="",
            offset="(3.7,0)",
            height=19,
            depth=19,
            width=2),

        tikzeng.to_Image(
            "image4",
            n_filer="",
            s_filer="96\\^{}3" if ADD_DIMENSIONS else "",
            offset="(4.2,0,0)",
            height=18.4,
            depth=18.4,
            width=2),

        tikzeng.to_Pool(
            name="pool_b2",
            s_filer="48\\^{}3" if ADD_DIMENSIONS else "",
            offset="(0,0,0)",
            to="(image4-east)",
            width=2,
            height=9.2,
            depth=9.2,
            opacity=0.5),

        ############# 3rd layer ############

        # tikzeng.to_Image(
        # "image5",
        # s_filer="",
        # n_filer=46,
        # offset="(6,0,0)",
        # height=9.2,
        # depth=9.2,
        # width=2),

        # tikzeng.to_connection("pool_b2", "image5"),

        tikzeng.to_Conv(
            "conv5",
            n_filer=128 if ADD_DIMENSIONS else "",
            s_filer="",
            offset="(6.5,0,0)",
            height=9.2,
            depth=9.2,
            width=2),

        tikzeng.to_connection("pool_b2", "conv5"),

        tikzeng.to_Conv(
            "conv6",
            n_filer="",
            s_filer="",
            offset="(7,0,0)",
            height=9,
            depth=9,
            width=2),

        tikzeng.to_Image(
            "image6",
            n_filer="",
            s_filer="44\\^{}3" if ADD_DIMENSIONS else "",
            offset="(7.5,0,0)",
            height=8.4,
            depth=8.4,
            width=2),

        tikzeng.to_Pool(
            name="pool_b3",
            s_filer="22\\^{}3" if ADD_DIMENSIONS else "",
            offset="(0,0,0)",
            to="(image6-east)",
            width=2,
            height=2.8,
            depth=2.8,
            opacity=0.5),

        ############# Bottleneck ############

        # tikzeng.to_Image(
        # "image7",
        # s_filer="",
        # n_filer=14,
        # offset="(9,0,0)",
        # height=2.8,
        # depth=2.8,
        # width=2),

        # tikzeng.to_connection("pool_b3", "image7"),

        tikzeng.to_Conv(
            "conv7",
            n_filer=256 if ADD_DIMENSIONS else "",
            s_filer="",
            offset="(9.5,0,0)",
            height=2.8,
            depth=2.8,
            width=2),

        tikzeng.to_connection("pool_b3", "conv7"),

        tikzeng.to_Conv(
            "conv8",
            n_filer="",
            s_filer="",
            offset="(10.0,0,0)",
            height=2.4,
            depth=2.4,
            width=2),

        tikzeng.to_Image(
            "image8",
            n_filer="",
            s_filer="18\\^{}3" if ADD_DIMENSIONS else "",
            offset="(10.5,0,0)",
            height=2,
            depth=2,
            width=2),

        # Encoder

        ############# 1st layer ############

        tikzeng.to_UnPool(
            name="unpool_b1",
            # s_filer=36,
            offset="(0.8,0,0)",
            to="(image8-east)",
            width=2,
            height=6.0,
            depth=6.0,
            opacity=0.5),

        tikzeng.to_connection("image8", "unpool_b1"),

        tikzeng.to_Image(
            "image9",
            s_filer="",
            n_filer="",
            offset="(12.1,0,0)",
            height=6.0,
            depth=6.0,
            width=2),

        tikzeng.to_skip(of='image6', to='image9', pos=1.25),

        tikzeng.to_Conv(
            "conv9",
            n_filer=128 if ADD_DIMENSIONS else "",
            s_filer="",
            offset="(12.6,0,0)",
            height=6.0,
            depth=6.0,
            width=2),

        tikzeng.to_Conv(
            "conv10",
            n_filer="",
            s_filer="",
            offset="(13.1,0,0)",
            height=5.6,
            depth=5.6,
            width=2),

        tikzeng.to_Image(
            "image10",
            n_filer="",
            s_filer="32\\^{}3" if ADD_DIMENSIONS else "",
            offset="(13.6,0,0)",
            height=5.2,
            depth=5.2,
            width=2),

        ############# 2nd layer ############

        tikzeng.to_UnPool(
            name="unpool_b2",
            # s_filer=64,
            offset="(0.8,0,0)",
            to="(image10-east)",
            width=2,
            height=10.4,
            depth=10.4,
            opacity=0.5),

        tikzeng.to_connection("image10", "unpool_b2"),

        tikzeng.to_Image(
            "image11",
            s_filer="",
            n_filer="",
            offset="(15.2,0,0)",
            height=10.4,
            depth=10.4,
            width=2),

        tikzeng.to_skip(of='image4', to='image11', pos=1.25),

        tikzeng.to_Conv(
            "conv11",
            n_filer=64 if ADD_DIMENSIONS else "",
            s_filer="",
            offset="(15.7,0,0)",
            height=10.4,
            depth=10.4,
            width=2),

        tikzeng.to_Conv(
            "conv12",
            n_filer="",
            s_filer="",
            offset="(16.2,0,0)",
            height=10,
            depth=10,
            width=2),

        tikzeng.to_Image(
            "image12",
            s_filer="60\\^{}3" if ADD_DIMENSIONS else "",
            n_filer="",
            offset="(16.7,0,0)",
            height=9.6,
            depth=9.6,
            width=2),

        ############# 3rd layer ############

        tikzeng.to_UnPool(
            name="unpool_b3",
            # s_filer=120,
            offset="(1.2,0,0)",
            to="(image12-east)",
            width=2,
            height=19.2,
            depth=19.2,
            opacity=0.5),

        tikzeng.to_connection("image12", "unpool_b3"),

        tikzeng.to_Image(
            "image13",
            s_filer="",
            n_filer="",
            offset="(18.7,0,0)",
            height=19.2,
            depth=19.2,
            width=2),

        tikzeng.to_skip(of='image2', to='image13', pos=1.25),

        tikzeng.to_Conv(
            "conv13",
            n_filer=32 if ADD_DIMENSIONS else "",
            s_filer="",
            offset="(19.2,0,0)",
            height=19.2,
            depth=19.2,
            width=2),

        tikzeng.to_Conv(
            "conv14",
            n_filer="",
            s_filer="",
            offset="(19.7,0,0)",
            height=18.8,
            depth=18.8,
            width=2),

        tikzeng.to_Image(
            "image14",
            s_filer="112\\^{}3" if ADD_DIMENSIONS else "",
            n_filer=12 if ADD_DIMENSIONS else "",
            offset="(20.2,0,0)",
            height=18.4,
            depth=18.4,
            width=2),
    ]
)

############# outputs ############

# tikzeng.to_Conv(
# "conv15",
# "",
# "",
# offset="(23.5,0,-3)",
# height=18.4,
# depth=18.4,
# width=2),

if ADD_INPUT_OUTPUT:
    arch.extend(
        [
            # tikzeng.to_Image(
                # "image15",
                # s_filer="size" if ADD_CAPTIONS else "",
                # n_filer=1 if ADD_DIMENSIONS else "",
                # offset="(24,0,-3)",
                # height=18.4,
                # depth=18.4,
                # width=1,
                # caption="LSD" if ADD_CAPTIONS else ""),
            # tikzeng.to_input(
                # 'imgs/lsd_size.png',
                # to="(23.8,-0.4,-4.05)",
                # width=3.66,
                # height=3.66),
            # tikzeng.to_connection("image14", "image15"),

            # tikzeng.to_Image(
                # "image16",
                # s_filer="offset to center" if ADD_CAPTIONS else "",
                # n_filer=9 if ADD_DIMENSIONS else "",
                # offset="(26,0,-3)",
                # height=18.4,
                # depth=18.4,
                # width=3,
                # caption="LSD" if ADD_CAPTIONS else ""),
            # tikzeng.to_input(
                # 'imgs/lsd_center.png',
                # to="(26.2,-0.4,-4.05)",
                # width=3.66,
                # height=3.66),



            # tikzeng.to_Conv(
            # "conv16",
            # "",
            # "",
            # offset="(23.5,-1.3,3.6)",
            # height=18.4,
            # depth=18.4,
            # width=2),

            tikzeng.to_Image(
                "image19",
                s_filer="",
                n_filer=2 if ADD_DIMENSIONS else "",
                offset="(22.8,0.0, 0.0)",
                height=18.4,
                depth=18.4,
                width=1,
                caption="Probability maps" if ADD_CAPTIONS else ""),
            tikzeng.to_input(
                'imgs/prob_map.png',
                to="(23.0,0.0,0.0)",
                width=3.66,
                height=3.66),
            tikzeng.to_connection("image14", "image19"),

            # Connetion input to first layer
            tikzeng.to_connection("image0", "conv1"),


        ]
    )


arch.append(tikzeng.to_end())


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    tikzeng.to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
