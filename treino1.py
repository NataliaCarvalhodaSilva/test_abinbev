from selenium import webdriver
#  abrindo a página
driver = webdriver.Firefox()
driver.get("https://test-bees.herokuapp.com/users/sign_in")
# inserindo email do usuário
campo_email = driver.find_element_by_id("user_email")
campo_email.send_keys("ftdranataliacarvalho@gmail.com")
# inserindo a senha do usuário
campo_senha = driver.find_element_by_id("user_password")
campo_senha.send_keys("BoYa0107*")
# escolhendo a opção de lembrar usuário e senha
campo_remember_me = driver.find_element_by_id("user_remember_me")
campo_remember_me.click()
botao_submit = driver.find_element_by_name("commit")
# acessando a conta 
botao_submit.click()
campo_de_confirmacao = driver.find_element_by_xpath("/html/body/div/p")
# confirmando que o acesso foi concluído com sucesso
mensagem_de_confirmacao = campo_de_confirmacao.text
assert mensagem_de_confirmacao == "Signed in successfully."
