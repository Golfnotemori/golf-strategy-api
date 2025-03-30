from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def generate_strategy_image(image_bytes, distance, deviation):
    bg = Image.open(BytesIO(image_bytes)).convert("RGB")
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(bg)
    x0, y0 = 100, 100
    xs = np.random.normal(x0 + distance, deviation, 100)
    ys = np.random.normal(y0, deviation, 100)
    ax.scatter(xs, ys, c='red', alpha=0.4)
    ax.plot(x0, y0, 'ko')
    buf = BytesIO()
    plt.axis('off')
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    buf.seek(0)
    return buf
