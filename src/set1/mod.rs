pub mod hextobase64;

use crate::common::challenge;

pub static challenges: [&'static challenge::Info; 1] = [
    &hextobase64::info,
];