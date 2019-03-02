# frozen_string_literal: true

require 'slop'
require './lib/roman_numeral/calculator'

puts RomanNumeral::Calculator.evaluate(ARGV[0])
