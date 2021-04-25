pub mod hex_to_base64;
pub mod fixed_xor;
pub mod single_byte_xor;
pub mod detect_single_xor;

use crate::common::challenge;

pub static CHALLENGES: [&'static challenge::INFO; 4] = [
    &hex_to_base64::INFO,
    &fixed_xor::INFO,
    &single_byte_xor::INFO,
    &detect_single_xor::INFO
];