pub mod hex_to_base64;
pub mod fixed_xor;

use crate::common::challenge;

pub static challenges: [&'static challenge::Info; 2] = [
    &hex_to_base64::info,
    &fixed_xor::info,
];