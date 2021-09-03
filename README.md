# Bit-Plane-Slicing-and-Quantization-Based-Color-Image-Watermarking-in-Spatial-Domain
You can find the source codes and algorithms proposed by this "Bit Plane Slicing and Quantization-Based Color Image Watermarking in Spatial Domain" study. The link of this article: https://link.springer.com/chapter/10.1007/978-981-16-0586-4_30

<b> <h3> Abstract </h3> </b>
In this paper, a robust and fast watermarking scheme in spatial domain is introduced to embed a color watermark image over a color host image. The host image was converted from RGB to YCbCr. The watermark image was compressed using bit plane slicing followed by embedding into the luminance channel of the host image. Quantization process with pseudo-random steps was incorporated to embed the watermark into the host image and minimize the security vulnerabilities in the watermarked image. The experimental results indicate that the proposed watermarking scheme has better performance compared to existing related works in terms of robustness, time complexity and invisibility.

<b> Keywords </b>
Arnold transform DC-coefficient of 2D discrete Fourier transform (2D-DFT) Quantization Bit plane slicing 

<b> Code </b>
<li> In arnold.py the implementation of <b> Arnold Transformation </b> which is one of the most used scrambling techniques to permute an image or signal can be found.
<li> In single_channel.py the implementation of two algorithms: 
  i. <b> Watermark Embedding Process </b> and ii. <b> Watermark Extraction Process </b>, proposed by this study can be found.
<li> In proposed_embed.py and proposed_extract.py the implementation of <b> Proposed Watermarking Technique proposed </b> (including <b> Pre-processing of the Host Image and Watermark Image </b> and "Post-processing the bit sequence </b>) by this study can be found.
