# frozen_string_literal: true

require_relative '../spec_helper'
require_relative '../../lib/roman_numeral/converter'

module RomanNumeral
  RSpec.describe Converter do
    conversions = [
      ['I', 1],
      ['II', 2],
      ['III', 3],
      ['IV', 4],
      ['V', 5],
      ['VI', 6],
      ['VII', 7],
      ['VIII', 8],
      ['IX', 9],
      ['X', 10],
      ['XI', 11],
      ['XIV', 14],
      ['XV', 15],
      ['XVI', 16],
      ['XIX', 19],
      ['XX', 20],
      ['XXX', 30],
      ['XL', 40],
      ['L', 50],
      ['LX', 60],
      ['LXX', 70],
      ['LXXX', 80],
      ['XC', 90],
      ['C', 100],
      ['CX', 110],
      ['CC', 200],
      ['CCC', 300],
      ['CD', 400],
      ['D', 500],
      ['DC', 600],
      ['DCC', 700],
      ['DCCC', 800],
      ['CM', 900],
      ['M', 1000],
      ['MCMLXVII', 1967],
      ['MM', 2000],
      ['MMXIX', 2019],
      ['MMM', 3000],
      ['MMMM', 4000],
      ['MMMMM', 5000]
    ]

    describe '.to_integer' do
      context 'when given a roman numeral' do
        conversions.each do |(roman_numeral, integer)|
          it "converts '#{roman_numeral}' into #{integer}" do
            expect(Converter.to_integer(roman_numeral)).to eq(integer)
          end
        end
      end

      context 'when given something other than a roman numeral' do
        it 'raises an error' do
          bad_inputs = [['V'], '(V)', 5, 'K', 'I V']
          bad_inputs.each do |input|
            expect { Converter.to_integer(input) }.to raise_error(ArgumentError)
          end
        end
      end
    end

    describe '.to_roman_numeral' do
      context 'when given an integer' do
        conversions.each do |(roman_numeral, integer)|
          it "converts #{integer} into '#{roman_numeral}'" do
            expect(Converter.to_roman_numeral(integer)).to eq(roman_numeral)
          end
        end
      end

      context 'when given something other than an integer' do
        it 'raises an error' do
          bad_inputs = [5.5, '5']
          bad_inputs.each do |input|
            expect { Converter.to_roman_numeral(input) }.to raise_error(ArgumentError)
          end
        end
      end
    end
  end
end
