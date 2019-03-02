# frozen_string_literal: true

require_relative '../spec_helper'
require_relative '../../lib/roman_numeral/converter'

module RomanNumeral
  RSpec.describe Converter do
    describe '.to_integer' do
      it "converts 'V' into 5" do
        expect(Converter.to_integer('V')).to eq(5)
      end
    end

    describe '.to_roman_numeral' do
      it "converts 5 into 'V'" do
        expect(Converter.to_roman_numeral(5)).to eq('V')
      end
    end
  end
end
