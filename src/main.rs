extern crate engiffen;

use engiffen::{load_images, engiffen, Gif, Quantizer};
use std::fs::File;


fn main() -> Result<(), Box<dyn std::error>> {
let image_paths = vec!["/home/mabbas/a/a/data/1.jpeg", "/home/mabbas/a/a/data/2.jpeg","/home/mabbas/a/a/data/3.jpeg", "/home/mabbas/a/a/data/4.jpeg", "/home/mabbas/a/a/data/5.jpeg","/home/mabbas/a/a/data/6.jpeg"];

let images = load_images(&image_paths);
let mut output = File::create("output.gif")?;

// encode an animated gif at 10 frames per second
let gif = engiffen(&images, 10, Quantizer::Naive)?;
gif.write(&mut output);

}