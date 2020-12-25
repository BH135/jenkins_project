from selenium.webdriver.common.by import By
"""以下为项目服务器地址"""
URL = "http://113.128.179.250:8020/tydt-cim/login"

"""以下为通用配置数据"""
# 点击cim进入系统
currency_cim = By.ID, "cim"
# iframe表单名称-0
currency_frame_name = "frmright"
# iframe表单名称-1
currency_frame_name1 = "layui-layer-iframe1"
# iframe表单名称-2
currency_frame_name2 = "layui-layer-iframe1"

"""以下为登录页面配置数据"""
# 用户名
login_username = By.NAME, "username"
# 密码
login_pwd = By.NAME, "password"
# 验证码
login_verify_code = By.NAME, "validateCode"
# 登录按钮
login_btn = By.ID, "btnSubmit"
# 获取登陆成功文本信息
login_err_info = By.CSS_SELECTOR, '.layui-nav.setbtn span span'

'''以下数据为知识库页面配置数据'''
# 头部信息
pay_my_prder_title = "/html/head/title"
# 知识库
kb = By.ID, "2079"
# 新增按钮
kb_newlyadded_btn = By.XPATH, '//*[@id="toolbar"]/a[1]'
# 标题
kb_title = By.NAME, "policyTitle"
# 类型
kb_type = By.XPATH, '//*[@id="form-policy-add"]/div[2]/div[1]/div/div/select/option[3]'
# 来源
kb_source = By.NAME, "policySource"
# 发布时间
kb_Releasetime = By.NAME, "policyTime"
kb_Selectdate = By.CSS_SELECTOR, "td.day.active"
# 上传文件
kb_Uploadfiles = By.ID, "fileBtn"
# 获取上传文件结果
kb_Uploadfiles_result = By.CSS_SELECTOR, "#upload-list tr#WU_FILE_0 td"
# 选择文件
kb_Selectfile = By.ID, "filePicker"
# 确定
kb_determine = By.CLASS_NAME, "layui-layer-btn0"
# 内容
kb_content = By.CLASS_NAME, "note-editable"
# 确定
kb_determine1 = By.CLASS_NAME, "layui-layer-btn0"
# 获取业务新增结果
kb_newlyadded_result = By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr/td[3]'
# 搜索标题
kb_search = By.NAME, 'policyTitle'
# 重置
kb_reset = By.CSS_SELECTOR, "a.btn.btn-warning.btn-reset"
# 获取搜索结果
kb_search_result = By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr/td[3]'
# 删除按键
kb_delete = By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr/td[7]/a[3]'
# 确定删除
kb_todelete = By.CLASS_NAME, "layui-layer-btn0"

'''以下为文件存储页面配置数据'''
# 文件存储
file_store = By.ID, "2078"
# 空间管理
file_store_management = By.LINK_TEXT, "空间管理"
# 新增
file_store_newly_added = By.CSS_SELECTOR, "a.btn.btn-table.btn-renew"
# 空间名称
file_store_space_name = By.ID, "bucketName"
# 确定
file_store_ok = By.CLASS_NAME, "layui-layer-btn0"
# 获取新增结果
file_store_new_results = By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr[6]/td[2]'
# 点击文件
file_store_file = By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr[6]/td[6]/a[2]'
# 点击上传
file_store_upload = By.XPATH, '//*[@id="toolbar"]/a[1]'
# 获取业务上传结果
file_store_upload_results = By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr/td[2]'
# 删除
file_store_file_deletion = By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr/td[6]/a[3]'
# 确定删除
file_store_confirm_delete = By.CLASS_NAME, "layui-layer-btn0"
# 点击重置
file_store_click_reset = By.CSS_SELECTOR, "a.btn.btn-warning.btn-reset"
# 删除
file_store_delete = By.XPATH, '//*[@id="bootstrap-table"]/tbody/tr[6]/td[6]/a[4]'

'''以下为资料管理页面配置数据'''
# 资料管理
management = By.ID, "2076"
# 新建文件夹
management_new_folder = By.CLASS_NAME, "icon-btn-add"
# 文件夹名称
management_foldername = By.ID, "itemName"
# 确定
management_determine = By.CLASS_NAME, "layui-layer-btn0"
# 获取业务新增结果
management_folder_results = By.XPATH, '//*[@id="document-content"]/dl/div/dd[1]/div[2]/a'
# 上传
management_upload = By.CLASS_NAME, "up-load"
# 获取上传业务上传结果
management_upload_results = By.XPATH, '//*[@id="document-content"]/dl/div/dd[4]/div[2]/a'
# 点击测试文件选项框
management_option_box = By.XPATH, '//*[@id="document-content"]/dl/div/dd[4]/span/div/label'
# 点击移动
management_move = By.CLASS_NAME, "other-move"
# 选择要移动文件夹的
management_move_folder = By.ID, "tree_4_a"
# 点击测试文件夹
management_test_folder = By.XPATH, '//*[@id="document-content"]/dl/div/dd[1]/div[2]/a'
# 获取业务移动结果
management_move_results = By.XPATH, '//*[@id="document-content"]/dl/div/dd[4]/div[2]/a'
# 点击返回上一级
management_the_next_level = By.CLASS_NAME, "go-back"
# 选择删除创建的测试业务-01
management_testing_business1 = By.XPATH, '//*[@id="document-content"]/dl/div/dd[1]/span/div/label'
# 选择删除创建的测试业务-02
management_testing_business2 = By.XPATH, '//*[@id="document-content"]/dl/div/dd[4]/span/div/label'
# 点击删除
management_click_delete = By.CLASS_NAME, "other-delete"
# 确定删除
management_confirm_delete = By.CLASS_NAME, "layui-layer-btn0"

