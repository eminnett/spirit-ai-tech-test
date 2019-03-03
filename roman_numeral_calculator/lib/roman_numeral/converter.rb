# frozen_string_literal: true

require_relative './validations'

module RomanNumeral
  # The Converter module handles the conversion of roman numerals to integers and vice versa.
  #
  # Example Usage:
  # RomanNumeral::Converter.to_integer('IX') => 9
  # RomanNumeral::Converter.to_roman_numeral(19) => 'XIX'
  module Converter
    extend Validations

    NUMERAL_MAPPING = [
      ['M', 1000],
      ['D', 500],
      ['C', 100],
      ['L', 50],
      ['X', 10],
      ['V', 5],
      ['I', 1]
    ].freeze

    def self.to_integer(roman_numeral)
      validate_string(roman_numeral)
      roman_numeral = roman_numeral.strip
      validate_roman_numeral(roman_numeral)

      integer = 0
      letters = roman_numeral.split('')
      letters.each_with_index do |letter, i|
        integer += letter_value(roman_numeral, letter, i, letters.count)
      end
      integer
    end

    def self.letter_value(roman_numeral, letter, index, num_letters)
      value = NUMERAL_MAPPING.assoc(letter)[1]

      if index < num_letters - 1
        next_letter = roman_numeral[index + 1]
        next_value = NUMERAL_MAPPING.assoc(next_letter)[1]
        return -value if [5 * value, 10 * value].include? next_value
      end

      value
    end
    private_class_method :letter_value

    def self.to_roman_numeral(integer)
      validate_integer(integer)
      roman_numeral = ''
      NUMERAL_MAPPING.each_with_index do |mapping, i|
        roman_numeral, integer = handle_additive_letters(roman_numeral, integer, mapping)
        roman_numeral, integer = handle_subtractive_letters(roman_numeral, integer, mapping, i)
      end
      roman_numeral
    end

    def self.handle_additive_letters(roman_numeral, integer, (letter, value))
      ratio = integer.to_f / value
      return [roman_numeral, integer] if ratio < 1

      ratio.floor.times do
        roman_numeral += letter
        integer -= value
      end
      [roman_numeral, integer]
    end
    private_class_method :handle_additive_letters

    def self.handle_subtractive_letters(roman_numeral, integer, (letter, value), index)
      ratio = integer.to_f / value
      leading_five = value.to_s[0] == '5'
      return [roman_numeral, integer] unless subtraction_required(leading_five, ratio)

      skip_index = leading_five ? 1 : 2
      subtraction_letter = NUMERAL_MAPPING[index + skip_index][0]
      term = subtraction_letter + letter
      [roman_numeral + term, integer - to_integer(term)]
    end
    private_class_method :handle_subtractive_letters

    def self.subtraction_required(leading_five, ratio)
      (leading_five && ratio >= 0.8) || (!leading_five && ratio >= 0.9)
    end
    private_class_method :subtraction_required
  end
end
