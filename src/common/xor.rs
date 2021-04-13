use std::collections::HashMap;
use std::char;

pub fn xor(input: &Vec<u8>, xor: &Vec<u8>) -> Vec<u8> {
    let mut result: Vec<u8> = Vec::new();

    let mut pos = 0;
    while pos < input.len() {
        result.push(input[pos] ^ xor[pos % xor.len()]);

        pos += 1;
    }

    result
}

pub fn character_count(input: &String) -> HashMap<String, i32> {
    let mut counter = HashMap::new();
    let char_vec: Vec<u8> = input.as_bytes().to_vec();

    let mut index = 0;
    while index < char_vec.len() {
        let character = char_vec[index] as char;
        let count = counter.entry(character.to_lowercase().to_string()).or_insert(0);
        *count += 1;

        index += 1;
    }

    counter
}

pub fn frequency_check(input: &String) -> f32 {
    let mut character_frequency: HashMap<String, f32> = HashMap::new();
    character_frequency.insert(String::from(' '), 13.000);
    character_frequency.insert(String::from('e'), 12.702);
    character_frequency.insert(String::from('t'), 9.056);
    character_frequency.insert(String::from('a'), 8.167);
    character_frequency.insert(String::from('o'), 7.507);
    character_frequency.insert(String::from('i'), 6.966);
    character_frequency.insert(String::from('n'), 6.749);
    character_frequency.insert(String::from('s'), 6.327);
    character_frequency.insert(String::from('h'), 6.094);
    character_frequency.insert(String::from('r'), 5.987);
    character_frequency.insert(String::from('d'), 4.253);
    character_frequency.insert(String::from('l'), 4.025);
    character_frequency.insert(String::from('c'), 2.782);
    character_frequency.insert(String::from('u'), 2.758);
    character_frequency.insert(String::from('m'), 2.406);
    character_frequency.insert(String::from('w'), 2.360);
    character_frequency.insert(String::from('f'), 2.228);
    character_frequency.insert(String::from('g'), 2.015);
    character_frequency.insert(String::from('y'), 1.974);
    character_frequency.insert(String::from('p'), 1.929);
    character_frequency.insert(String::from('b'), 1.492);
    character_frequency.insert(String::from('v'), 0.978);
    character_frequency.insert(String::from('k'), 0.772);
    character_frequency.insert(String::from('j'), 0.153);
    character_frequency.insert(String::from('x'), 0.150);
    character_frequency.insert(String::from('q'), 0.095);
    character_frequency.insert(String::from('z'), 0.074);

    let mut diff: f32 = 0.0;
    let char_count = character_count(&input);

    for (chr, count) in char_count.iter() {
        let frequency = (count / input.len() as i32) as f32 * 100.0;

        diff += match character_frequency.get(chr) {
            None => -10.0,
            Some(val) => (frequency - val).abs()
        };
    }

    diff
}

pub fn find_best_xor_match(input: &Vec<u8>) -> Option<String> {
    let mut score = 0.0;
    let mut best_match: Option<String> = None;

    for index in 0..256 {
        match char::from_u32(index) {
            Some(character) => {
                match String::from_utf8(xor(input, &vec![character as u8])) {
                    Ok(result) => {
                        let new_score = frequency_check(&result);
                        if new_score > score {
                            score = new_score;
                            best_match = Some(result);
                        }
                    },
                    Err(_error) => {}
                };
            },
            _ => {}
        };
    }

    best_match
}