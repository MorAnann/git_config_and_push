import subprocess
import sys

def set_git_identity(name, email, global_config=True):
    """
    设置 Git 用户名和电子邮件地址。
    :param name: 用户名
    :param email: 用户的电子邮件地址
    :param global_config: 是否为全局配置（默认为 True）
    """
    try:
        # 如果是全局配置，则加上 --global
        if global_config:
            subprocess.run(["git", "config", "--global", "user.name", name], check=True)
            subprocess.run(["git", "config", "--global", "user.email", email], check=True)
        else:
            subprocess.run(["git", "config", "user.name", name], check=True)
            subprocess.run(["git", "config", "user.email", email], check=True)
        print(f"Git identity set to:\nName: {name}\nEmail: {email}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting Git identity: {e}")
        sys.exit(1)

def set_remote_repository(remote_url):
    """
    设置 Git 远程仓库地址
    :param remote_url: 远程仓库的 URL 地址（如 SSH 或 HTTPS）
    """
    try:
        # 检查是否已存在名为 'origin' 的远程仓库
        result = subprocess.run(["git", "remote"], capture_output=True, text=True, check=True)
        remotes = result.stdout.splitlines()
        
        if "origin" in remotes:
            # 如果存在，则更新地址
            subprocess.run(["git", "remote", "set-url", "origin", remote_url], check=True)
            print(f"Remote repository URL updated to: {remote_url}")
        else:
            # 如果不存在，则添加新的远程仓库
            subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
            print(f"Remote repository URL added: {remote_url}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting remote repository URL: {e}")
        sys.exit(1)


def git_commit(message):
    """
    提交 Git 修改
    :param message: 提交信息
    """
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        print(f"Changes committed with message: {message}")
    except subprocess.CalledProcessError as e:
        print(f"Error committing changes: {e}")
        sys.exit(1)

def git_push():
    """
    推送代码到远程仓库
    """
    try:
        subprocess.run(["git", "push", "-u", "origin", "master"], check=True)
        print("Changes pushed to GitHub repository.")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing changes: {e}")
        sys.exit(1)

def main():
    # 用户输入设置
    name = input("Enter your Git name: ")
    email = input("Enter your Git email: ")
    commit_message = input("Enter commit message: ")
    remote_url = input("Enter the remote repository URL (SSH or HTTPS): ")

    # 设置 Git 用户信息
    set_git_identity(name, email)

    # 设置远程仓库地址
    set_remote_repository(remote_url)

    # 提交代码
    git_commit(commit_message)

    # 推送到远程仓库
    git_push()

if __name__ == "__main__":
    main()
