# Bit-Plane-Slicing-and-Quantization-Based-Color-Image-Watermarking-in-Spatial-Domain
You can find the source codes and algorithms proposed by this <b> "Bit Plane Slicing and Quantization-Based Color Image Watermarking in Spatial Domain" </b> study. The link of this article: https://link.springer.com/chapter/10.1007/978-981-16-0586-4_30

<b> <h3> Abstract </h3> </b>
In this paper, a robust and fast watermarking scheme in spatial domain is introduced to embed a color watermark image over a color host image. The host image was converted from RGB to YCbCr. The watermark image was compressed using bit plane slicing followed by embedding into the luminance channel of the host image. Quantization process with pseudo-random steps was incorporated to embed the watermark into the host image and minimize the security vulnerabilities in the watermarked image. The experimental results indicate that the proposed watermarking scheme has better performance compared to existing related works in terms of robustness, time complexity and invisibility.

<b> <h3> Keywords </h3> </b>
Arnold transform DC-coefficient of 2D discrete Fourier transform (2D-DFT) Quantization Bit plane slicing 

<b> <h3> Code </h3> </b>
<li> In arnold.py the implementation of <b> Arnold Transformation </b> which is one of the most used scrambling techniques to permute an image or signal can be found.
<li> In single_channel.py the implementation of two algorithms: 
  i. <b> Watermark Embedding Process </b> and ii. <b> Watermark Extraction Process </b>, proposed by this study can be found.
<li> In proposed_embed.py and proposed_extract.py the implementation of <b> Proposed Watermarking Technique proposed </b> (including <b> Pre-processing of the Host Image and Watermark Image </b> and <b> Post-processing the bit sequence </b>) by this study can be found.
  
<b> <h3> Experimental Results </h3> </b>
<li> Host images: (a) Avion, (b) Baboon, (c) Lena, (d) Peppers and (e) Sailboat
  <img src="https://user-images.githubusercontent.com/55454660/131952995-c0039e9b-7d2b-4fa2-b64f-2d7778096899.jpg" alt="Can't display it this time">

  
<li>  Color watermark image
  <img src="https://user-images.githubusercontent.com/55454660/131953079-dac3bfc9-0556-4b49-9a0c-52b370aa3666.jpg" alt="Can't display it this time">
  
  
<li> Extracted watermark images from watermarked images after different attacks.
  <img src="https://user-images.githubusercontent.com/55454660/131953093-ab4d4681-8c8a-4f9f-882d-47e4421e4ca4.jpg" alt="Can't display it this time">

  
<li> <b> Average time for Watermark Embedding / Extraction Time is found 0.3445/0.2700 which outperforms the existence works hence the proposed mmethod can be implement in real-time applications. </b>
  
  
