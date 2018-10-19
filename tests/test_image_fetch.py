from venus import venus 
import os
import pytest


def test_fetch_img():
    img = venus.get_wall()
    # check if image was downloaded
    assert os.stat(img).st_size != 0 
