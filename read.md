# 연결된 깃허브 레퍼지토리 저장소 확인
git remote -v

# 깃허브 레퍼지토리와 연결하기
git remote add origin ""

# 깃허브에 폴더 및 파일 올리기
git add .

# 커밋메세지와 함께 올리기
git commit -m "커밋메세지"

# 모든사항을 add 하고 커밋메세지와 함께 올리기
git commit -am "커밋메세지"

# 연결 된 원격 저장소에 최종 업로드
git push origin main

# 저장소에서 가져오기
git pull origin main

# git이 인식했는지 확인 명령어
git status

# commit 내역 확인
git log
git log --oneline = 더욱 상세하게 확인

# history
터미널 명령어 내역 확인

# reset을 이용한 커밋 되돌리기
git reset --hard [해시값]