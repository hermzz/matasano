use std::collections::HashMap;
use std::char;
use std::fmt;

pub fn xor(input: &Vec<u8>, xor: &Vec<u8>) -> Vec<u8> {
    let mut result: Vec<u8> = Vec::new();

    let mut pos = 0;
    while pos < input.len() {
        result.push(input[pos] ^ xor[pos % xor.len()]);

        pos += 1;
    }

    result
}

pub fn character_count(input: &Vec<u8>) -> HashMap<u8, i32> {
    let mut counter = HashMap::new();

    for chr in 'a'..'z' {
        counter.insert(chr as u8, 0);
    }

    let mut index = 0;
    while index < input.len() {
        let character = input[index] as char;
        let count = counter.entry(character.to_ascii_lowercase() as u8).or_insert(0);
        *count += 1;

        index += 1;
    }

    counter
}

fn char_score(chr: char) -> f32 {
    match chr {
        ' ' => 13.000,
        'e' => 12.702,
        't' => 9.056,
        'a' => 8.167,
        'o' => 7.507,
        'i' => 6.966,
        'n' => 6.749,
        's' => 6.327,
        'h' => 6.094,
        'r' => 5.987,
        'd' => 4.253,
        'l' => 4.025,
        'c' => 2.782,
        'u' => 2.758,
        'm' => 2.406,
        'w' => 2.360,
        'f' => 2.228,
        'g' => 2.015,
        'y' => 1.974,
        'p' => 1.929,
        'b' => 1.492,
        'v' => 0.978,
        'k' => 0.772,
        'j' => 0.153,
        'x' => 0.150,
        'q' => 0.095,
        'z' => 0.074,
        '\'' => 0.0,
        '0'..='9' => 0.0,
        _ => 10.0
    }
}

fn relative_score(input: &Vec<u8>, chr: u8, frequency: i32) -> f32 {
    let score = frequency as f32 / input.len() as f32 * 100.0;
    (score - char_score(chr as char)).abs()
}

pub fn frequency_check(input: &Vec<u8>) -> f32 {
    let mut diff = 0.0;
    let char_count = character_count(input);

    for (chr, frequency) in char_count {
        diff += relative_score(input, chr, frequency);
    }

    diff
}

#[derive(Debug)]
pub struct Match {
    pub result: String,
    pub score: f32
}

impl fmt::Display for Match {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.result, self.score)
    }
}

pub fn range_check(input: &Vec<u8>) -> bool {
    let mut has_space = false;
    for chr in input.clone().into_iter() {
        match chr {
            9 => {},
            10 => {},
            13 => {},
            32 ..= 126 => {},
            _ => return false
        }

        if chr == ' ' as u8 {
            has_space = true;
        }
    }

    has_space && true
}

pub fn find_best_xor_match(input: &Vec<u8>) -> Option<Match> {
    let mut best_match = Match { result: String::from(""), score: 0.0 };

    for index in 0u8..=255 {
        let result = xor(input, &vec![index]);
        if range_check(&result) {
            let new_score = frequency_check(&result);
            let readable_result: String = result.iter().map(|b| *b as char).collect::<Vec<_>>().into_iter().collect();
            if best_match.result.len() == 0 || new_score < best_match.score {
                best_match = Match { result: readable_result, score: new_score };
            }
        }
    }

    if best_match.result.len() > 0 {
        Some(best_match)
    } else {
        None
    }
}