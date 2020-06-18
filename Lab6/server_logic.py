import re


class Parser:

    def __init__(self):
        self.expr_list = []
        regexp = "[()]|[0-7]+\.[0-7]+|[0-7]+|[+]|[\-]|[*]|[/]|[\^]|sin|cos"
        self.regexp = re.compile(regexp)

    def _parse(self, data: str):
        self.expr_list = re.findall(self.regexp, data)

    def _check_parentheses(self) -> bool:
        return self.expr_list.count('(') == self.expr_list.count(')')

    def _check_illegal_characters(self, data):
        return len("".join(self.expr_list)) == len(data)


    def _calculate(self, data: str) -> str:
        operations = {
            r'sin': 'math.sin',
            r'cos': 'math.cos',
            r'\^': '**'
        }

        number = "[0-7]+\.[0-7]+|[0-7]+"
        # производим подстановку выражений
        for regexp, repl in operations.items():
            data = re.sub(regexp, repl, data)

        data = re.sub(number, self.convert_float_to_decimal, data)


        try:
            out = eval(data)
            print('Отправлено:', out)
            return self.convert_decimal_to_oct(out)

        except ZeroDivisionError as error:
            return "Деление на 0"


    def process(self, data) -> str:

        error_response = ""
        success_check = True
        self._parse(data)
        if not self._check_parentheses():
            error_response += "Непарные скобки\n"
            success_check = False
        if not self._check_illegal_characters(data):
            error_response += "Ошибка распознавания выражения\n"
            success_check = False

        if success_check:
            resp = self._calculate(data)
            return resp
        else:
            return error_response


    def convert_float_to_decimal(self, number):
        number = number[0]

        number = number.split('.')
        number_integer_part = number[0]

        # Расчет целой части
        integer_results = 0
        for each_digit in enumerate(reversed(number_integer_part)):
            result = int(each_digit[1]) * (8 ** each_digit[0])
            print("{} * {}^{} = {}".format(
                each_digit[1], 8, each_digit[0], result))

            integer_results += result

        final_result = integer_results

        if len(number) > 1:
            number_float_part = number[1]

        # Расчет дробной части

            negative_length = (0 - len(number_float_part))
            number_float_part = number_float_part[::-1]


            number_float_part_reversed = []
            for number in number_float_part:
                number_float_part_reversed.append(number)

            float_results = 0
            for index in range(negative_length, 0):
                result = int(number_float_part_reversed[index]) * (8 ** index)
                print("{} * {}^{} = {}".format(
                    number_float_part_reversed[index], 8, index, result))
                float_results += result

            final_result += float_results


        return str(final_result)

    def convert_decimal_to_oct(self, f, n=4):

        whole = int(f)
        rem = (f - whole) * 8
        int_ = int(rem)
        rem = (rem - int_) * 8
        octals = [str(abs(int_))]
        count = 1

        while rem and count < n:
            count += 1
            int_ = int(rem)
            rem = (rem - int_) * 8
            octals.append(str(abs(int_)))
        return "{:o}.{}".format(whole, "".join(octals))



