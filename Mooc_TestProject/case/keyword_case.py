import sys
sys.path.append("F:\Projects\Projects\Mooc_TestProject")
from util.excel_util import ExcelUtil
from keywords.actionMethod import ActionMethod

class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        """
        # 拿到行数
        # 循环行数，执行每一行case
        # 是否执行
            # 拿到执行方法
            # 拿到操作值
            # 拿到输入数据
            # 是否有输入数据
                # 执行方法（输入数据，操纵元素）
            # 没有输入数据
                # 执行方法（操纵元素）
        """
        handle_excel = ExcelUtil("F:\Projects\Projects\Mooc_TestProject\config\keyword2.xls")
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                handle_excel.write_value(i, "test")
                is_run = handle_excel.get_col_value(i, 3)
                print(is_run)
                if is_run == "yes":
                    method = handle_excel.get_col_value(i, 4)
                    send_value = handle_excel.get_col_value(i, 5)
                    handle_value = handle_excel.get_col_value(i, 6)
                    except_result_method = handle_excel.get_col_value(i, 7)
                    except_result = handle_excel.get_col_value(i, 8)
                    self.run_method(method,send_value,handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_result[0] == 'text':
                            print("---->", except_result_method)
                            result = self.run_method(except_result_method)
                            print("---->", result)
                            if except_value[1] in result:
                                handle_excel.write_value(i, "pass")
                            else:
                                handle_excel.write_value(i,"fail")
                        elif except_value[0] == "element":
                            result= self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,"pass")
                            else:
                                handle_excel.write_value(i,"fail")
                        else:
                            print("没else")
                    else:
                        print("预期结果为空")



    # 获取预期结果值
    def get_except_result_value(self,data):
        return data.split("=")


    def run_method(self,method,send_value='',handle_value=''):
        method_value = getattr(self.action_method,method)
        print(method)
        if method == 'get_url':
            result = method_value(send_value)
        elif method == "element_send_keys":
            result = method_value(send_value,handle_value)
        elif method == "click_element":
            result = method_value(handle_value)
        else:
            result = method_value()
        return result

if __name__ == "__main__":
    test = KeywordCase()
    test.run_main()