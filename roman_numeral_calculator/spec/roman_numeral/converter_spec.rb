# frozen_string_literal: true

require_relative '../spec_helper'
require_relative '../../lib/roman_numeral/converter'

module RomanNumeral
  RSpec.describe Converter do
    describe '.to_integer' do
      context 'when given a roman numeral' do
        it "converts 'V' into 5" do
          expect(Converter.to_integer('V')).to eq(5)
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
        it "converts 5 into 'V'" do
          expect(Converter.to_roman_numeral(5)).to eq('V')
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
