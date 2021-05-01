pub mod problem01;
pub mod problem02;
pub mod problem03;
pub mod problem04;
pub mod problem05;
pub mod problem06;

use crate::common::challenge;

pub static CHALLENGES: [&'static challenge::INFO; 6] = [
    &problem01::INFO,
    &problem02::INFO,
    &problem03::INFO,
    &problem04::INFO,
    &problem05::INFO,
    &problem06::INFO
];