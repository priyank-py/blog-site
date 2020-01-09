// const searchField = document.querySelector("#search-text");
const results = document.querySelector(".results");
const render = datas => {
  let html = datas
    .map(data => {
      return `<li class="card">
        <div>${data.title}</div>
        <small>${data.writer}</small>
      </li>`;
    })
    .join("");
  results.innerHTML = html;
  console.log(html);
};

const getData = async txt => {
  const response = await fetch(url);
  const datas = await response.json();

  //   return datas;
  const filteredData = await datas.filter(data => {
    const regex = new RegExp(`^${txt}`, "ig");
    if (data.title.match(regex) || data.writer.match(regex)) {
      return true;
    }
  });
  return filteredData;
};

searchField.addEventListener("keyup", e => {
  const searchText = searchField.value;
  getData(searchText)
    .then(data => render(data))
    .catch(err => console.log(err));

  if (searchText === "" || searchText === null) {
    results.innerHTML = "";
  }
});
