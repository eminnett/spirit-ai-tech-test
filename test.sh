echo '***** PYTHON TESTS *****'
pytest -v
echo '***** PYTHON LINTING *****'
pylint ./**/*.py
echo '***** RUBY TESTS *****'
bundle exec rspec roman_numeral_calculator
echo '***** RUBY LINTING *****'
rubocop