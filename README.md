# Card_Replicator
Utility to Replicate Standard 3.375 × 2.125 inch PVC Cards using a Canon TS9120


## Process

### Step 1

A card is placed onto the scanner in any orientation.  Using scanline we can save the results from the flatbed scanner to as a JPEG.

<p>
  <img src="static/1.png" width="500px"/>
</p>


### Step 2

We remove the background to make the image transparent, and apply a mask to remove noise that may be present from the scan.

<p>
  <img src="static/2.png" width="500px"/>
</p>

### Step 3

We use the "Unrotate" script created by Fred Weinhaus to rotate the card.  This tool accurately fixes images where the card is rotated more than 5 degrees.

<p>
  <img src="static/3.jpg" width="500px"/>
</p>

### Step 4

We once again apply a filter to more accurately remove the background from the image.

<p>
  <img src="static/4.png" width="500px"/>
</p>

### Step 5

We deskew the image to ensure the card is not slanting too far in one direction.  Deskew generally fixes cases where the card is rotated ~5 degrees and it adds an extra level of presision when fixing unwanted slanting in the image produced by Unrotate.

<p>
  <img src="static/5.png" width="500px"/>
</p>