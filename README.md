# 🚀 Projeto BMVC – Nível 3  
Sistema web em Python usando o microframework **Bottle**, seguindo o padrão **MVC**.  
Este projeto implementa **login com sessão**, **página restrita**, **CRUD completo** de um modelo próprio e **páginas HTML/TPL com CSS e JavaScript** totalmente funcionais.

---

## 📌 Funcionalidades do Projeto

### 🔐 Sistema de Login
- Autenticação de usuário com sessão.
- Redirecionamento automático para o login quando usuário não está autenticado.
- Página restrita acessível somente após login.

### 📄 CRUD Completo – *Planos de Treino*
O projeto implementa um CRUD funcional do modelo **Plano**:
- **Criar** plano de treino  
- **Listar** planos  
- **Editar** plano  
- **Excluir** plano  
- Todos os dados são gerenciados via lista de objetos Python no servidor.

### 🎨 Interface com HTML, CSS e JS
- Templates `.tpl` usando Bottle.
- Arquivos CSS e JS externos carregados pela rota `/static`.
- Páginas organizadas, estilizadas e funcionais. 
