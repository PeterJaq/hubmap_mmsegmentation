from .builder import DATASETS
from .custom import CustomDataset



@DATASETS.register_module()
class HuBMAPDataset(CustomDataset):
    """HuBMAP dataset.

    In segmentation map annotation for LoveDA, 0 is the ignore index.
    ``reduce_zero_label`` should be set to True. The ``img_suffix`` and
    ``seg_map_suffix`` are both fixed to '.png'.
    """

    CLASSES = ('background', 'positive')

    PALETTE = [[0, 0, 0], [1, 1, 1]]

    def __init__(self, **kwargs):
        super(HuBMAPDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)

