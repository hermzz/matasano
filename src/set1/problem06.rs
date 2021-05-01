use crate::common::challenge;
use crate::common::text;

pub static INFO: challenge::INFO = challenge::INFO {
    no:         6,
    title:      "Break repeating-key XOR",
    help:       "",
    execute_fn: interactive
};

pub fn interactive() -> i32 {
    text::hamming(
        String::from("this is a test").as_bytes().to_vec(),
        String::from("wokka wokka!!!").as_bytes().to_vec()
    );

    exit_ok!()
}
