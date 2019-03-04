echo '***** PYTHON TESTS *****'
pipenv run python -m pytest -v ..
echo '***** PYTHON LINTING *****'
pipenv run python -m pylint ../**/*.py
echo '***** RUBY TESTS *****'
cd ../roman_numeral_calculator
bundle exec rspec
echo '***** RUBY LINTING *****'
rubocop