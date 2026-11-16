import numpy as np
def generate_anchors(feature_size: int, image_size: float, scales: list[float], aspect_ratios: list[float]) -> list[list[float]]:
    """
    Returns a list of [x1, y1, x2, y2] anchor boxes.
    """
    # Write code here
    stride = image_size/feature_size
    anchor = []
    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j + 0.5)*stride
            cy = (i + 0.5)*stride
            for scale in scales:
                for ratio in aspect_ratios:
                    w=scale*np.sqrt(ratio)
                    h=scale/np.sqrt(ratio)

                    x1 = cx - w/2
                    x2 = cx + w/2
                    y1 = cy - h/2
                    y2 = cy + h/2

                    anchor.append([x1, y1, x2, y2] )
    return anchor
                    