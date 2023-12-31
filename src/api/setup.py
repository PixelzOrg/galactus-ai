"""
Setup file for Jarvis API.
"""

from setuptools import setup

setup(
    name="jarvis",
    packages=[
        "app.jarvis",
        "app.jarvis.diffusion",
        "app.jarvis.models",
        "app.jarvis.models.generation",
        "app.jarvis.models.nerf",
        "app.jarvis.models.nerstf",
        "app.jarvis.models.nn",
        "app.jarvis.models.stf",
        "app.jarvis.models.transmitter",
        "app.jarvis.rendering",
        "app.jarvis.rendering.blender",
        "app.jarvis.rendering.raycast",
        "app.jarvis.util",
    ],
    install_requires=[
        "filelock",
        "flask",
        "Pillow",
        "torch",
        "fire",
        "humanize",
        "requests",
        "tqdm",
        "matplotlib",
        "scikit-image",
        "scipy",
        "numpy",
        "blobfile",
        "pyyaml",
        "ipywidgets",
        "pygltflib",
        "python-dotenv",
        "clip @ git+https://github.com/openai/CLIP.git",
    ],
    author="OpenAI + Pixelz",
)
