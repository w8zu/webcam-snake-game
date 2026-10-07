# 🐍 웹캠 뱀게임 (Webcam Snake Game)

Google Teachable Machine의 웹캠 이미지 인식 모델을 사용하여 손 제스처로 조종하는 웹 기반 뱀게임입니다.

## 📋 프로젝트 개요

- **기술**: HTML5, Canvas, TensorFlow.js, Google Teachable Machine
- **모델**: Teachable Machine 커스텀 이미지 분류 모델
- **인식 클래스**: `neutral`, `left`, `right`, `up`, `down`
- **실시간 처리**: 웹캠 영상을 실시간으로 분석하여 게임 조종

## 🎮 게임 규칙

1. **목표**: 주황색 먹이(🍎)를 먹어서 점수를 올리기
2. **조종**: 웹캠에 보이는 손 제스처로 뱀 방향 제어
   - **left** (왼손): 뱀이 왼쪽으로 이동
   - **right** (오른손): 뱀이 오른쪽으로 이동
   - **up** (손을 위로): 뱀이 위로 이동
   - **down** (손을 아래로): 뱀이 아래로 이동
   - **neutral** (아무 제스처 안 함): 뱀 방향 유지
3. **게임 오버**: 뱀이 자신의 몸에 부딪혔을 때

## 🚀 사용 방법

### 1. 로컬에서 실행

```bash
# 파일 다운로드
git clone https://github.com/your-username/webcam-snake-game.git
cd webcam-snake-game

# 로컬 서버 실행 (Python)
python -m http.server 8000

# 브라우저에서 열기
# http://localhost:8000
```

### 2. 웹 브라우저에서 직접 실행

1. `index.html` 파일을 브라우저에서 열기
2. **"웹캠 시작"** 버튼 클릭
3. 웹캠 권한 허용
4. 손 제스처로 뱀 조종 시작!

### 3. 온라인 호스팅 (GitHub Pages)

```bash
# 이 저장소를 포크 또는 클론
git clone https://github.com/your-username/webcam-snake-game.git

# GitHub 설정에서 Pages 활성화
# 메인 브랜치 선택 후 저장

# 접속: https://your-username.github.io/webcam-snake-game
```

## 📊 작동 원리

### 1. 모델 로드
```
Google Teachable Machine 모델
    ↓
TensorFlow.js로 브라우저에서 로드
    ↓
웹캠 프레임마다 예측 수행
```

### 2. 실시간 인식 흐름

```
웹캠 캡처 (매 프레임)
    ↓
모델 예측 (5개 클래스 확률)
    ↓
가장 높은 확률의 클래스 선택
    ↓
뱀 방향 제어
    ↓
Canvas에 게임 렌더링
```

### 3. 게임 루프

```
매 100ms마다:
  - 뱀 머리 이동
  - 충돌 감지
  - 먹이 먹음 판정
  - 화면 업데이트
```

## 🎯 화면 구성

### 좌측 (웹캠 패널)
- 웹캠 라이브 영상
- 모델 인식 결과 (5개 클래스별 확률)
- 현재 인식된 제스처 표시
- 웹캠 시작/중지 버튼

### 우측 (게임 패널)
- 게임 화면 (400x400 Canvas)
- 현재 점수
- 뱀 길이
- 현재 이동 방향
- 방향 표시 (↑↓←→)
- 게임 상태 (진행중/게임오버)

## 🛠️ 기술 스택

### 프론트엔드
- **HTML5**: 페이지 구조
- **CSS3**: 반응형 디자인 (모바일 대응)
- **Canvas API**: 게임 렌더링

### 머신러닝
- **TensorFlow.js**: 브라우저에서 모델 실행
- **Google Teachable Machine**: 커스텀 이미지 분류 모델
- **Web API**: `getUserMedia()` (웹캠 접근)

## 📦 파일 구조

```
webcam-snake-game/
├── index.html          # 메인 HTML 파일 (전체 코드 포함)
├── server.py          # 로컬 서버 (선택사항)
├── README.md          # 이 파일
└── LICENSE            # MIT License
```

## ⚙️ 설정 커스터마이징

### 게임 속도 조정
`index.html`에서 다음 줄을 수정:
```javascript
const GAME_SPEED = 100; // 밀리초 (작을수록 빠름)
```

### 보드 크기 변경
```javascript
const GRID_SIZE = 20; // 20x20 그리드 (줄이면 큰 블록)
```

### 점수 설정
```javascript
score += 10; // 먹이당 획득 점수
```

## 🎓 학습 용도

이 프로젝트는 다음을 학습하는 데 유용합니다:
- **머신러닝**: 이미지 분류 모델 활용
- **웹 개발**: HTML5 Canvas, 실시간 처리
- **게임 개발**: 게임 루프, 충돌 감지
- **Web API**: getUserMedia, requestAnimationFrame

## 🐛 문제 해결

### "tmImage is not defined" 오류
- 원인: Teachable Machine 라이브러리 로드 실패
- 해결: 인터넷 연결 확인, 브라우저 캐시 삭제 후 새로고침

### 웹캠이 보이지 않음
- 웹캠 권한 확인 (브라우저 설정)
- HTTPS 또는 localhost에서만 작동 (보안 정책)

### 모델이 인식하지 못함
- Teachable Machine 모델 재학습 필요
- 조명 환경 확인
- 웹캠 품질 확인

## 📝 커스텀 모델 만들기

1. https://teachablemachine.withgoogle.com 방문
2. "이미지 프로젝트" 생성
3. 5개 클래스로 학습:
   - `neutral`: 손을 보이지 않는 상태
   - `left`: 왼손 (또는 왼쪽 제스처)
   - `right`: 오른손 (또는 오른쪽 제스처)
   - `up`: 손을 위로 올린 상태
   - `down`: 손을 아래로 내린 상태
4. 모델 내보내기 (Tensorflow.js 형식)
5. `index.html`의 `URL` 변수 변경:
   ```javascript
   const URL = 'your-teachable-machine-model-url/';
   ```

## 📄 라이선스

MIT License - 자유롭게 사용, 수정, 배포 가능

## 🤝 기여

버그 리포트나 개선 사항은 이슈 또는 풀 리퀘스트로 제출해주세요.

## 📧 문의

질문이나 제안사항이 있으면 이슈를 생성해주세요.

---

**즐거운 게임 되세요! 🎮🐍**
