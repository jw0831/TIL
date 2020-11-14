### MacOS Catalina

#### 버전 10.15.6

# 현재 Git Branch 명을 터미널 Prompt에 표시하기

- 안녕하세요, 제가 알려드릴 기능은 .git이 존재하는 디렉토리 영역으로 이동하면, 현재 작업하고 있는 branch 이름이 출력되도록 하는 기능 입니다.

- 하지만 제가 이 방법을 알아보았을 당시에, 대부분의 맥 사용자 분들의 Prompt 는 `%`표시가 아니라 `$`표시로 터미널 창에 보여집니다.

- 여러 시행착오 끝에 서로 다른 문구가 보여지는 것은 별 차이가 없지만, 설정을 하기위해서는 이해가 필요합니다.

- 본인의 `terminal.app` 에서 `$` = **bash** , `%` =  **zsh** 라는 차이점을 알고 시작하시면 되겠습니다.

- 저와 같은 경우는 zsh 입니다. 그리고 아직 *branch* 이름이 보이지 않습니다.

  ![zsh](https://user-images.githubusercontent.com/46684150/93518702-2754b800-f968-11ea-87c7-248997a55e0a.png)

## `$` bash 일 경우 설정 방법

- [bash 설정 방법 블로그](https://uroa.tistory.com/62)



## `%` zsh 일 경우 설정 방법

1. 터미널을 실행합니다

2. 텍스트 파일을 만들어 줍니다.

   ```shell
   touch .zshrc
   ```

3. 생성한 파일은 숨어있는 파일이므로, `Finder` 에서 숨겨진 파일이 보이도록 설정 합니다.

4. 다음과 같이 작성해 줍니다.

   ```shell
   # Load version control information
   autoload -Uz vcs_info
   precmd() { vcs_info }
   
   # Format the vcs_info_msg_0_ variable
   zstyle ':vcs_info:git:*' formats 'on branch %b'
    
   # Set up the prompt (with git branch name)
   setopt PROMPT_SUBST
   PROMPT='%n in ${PWD/#$HOME/~}  > '
   RPROMPT=\$vcs_info_msg_0_ 
   
   #PROMPT='%n in ${PWD/#$HOME/~} ${vcs_info_msg_0_} > ' #왼쪽에 다보여주는 옵션
   #RPROMPT=\$vcs_info_msg_0_ #오른쪽에 브랜치 보여주는 옵션
   ```

   ![zshrc](https://user-images.githubusercontent.com/46684150/93518687-23289a80-f968-11ea-8f3b-60fa6a96bf11.png)

5. 입력후 저장을 해줍니다.

6. 터미널에 명령어를 입력후 실행합니다.

   ```shell
   source ~/.zshrc
   ```

7. 축하드립니다~ 성공하셨을 경우 다음과 같이 보이게 됩니다. 
(우측에 보이는 설정을 통하여, 현재 마스터 브랜치에서 작업 하는것을 알 수 있습니다.)
   
   ![branch](https://user-images.githubusercontent.com/46684150/93518696-26238b00-f968-11ea-8aa0-8852feca43fa.png)



#### .gitignore 파일을 추가하여 .DS_Store와 같은 원치않는 파일들을 정규표현식처럼 마스킹 할 수 있다.

- .git이 위치한 경로에서 명령어: touch .gitignore
- open .gitignore를 해서, 원치않는 "파일명" 또는 "경로/" 등을 추가하자!

### Reference

[Add Git branch information to your ZSH prompt](https://www.themoderncoder.com/add-git-branch-information-to-your-zsh-prompt/)

